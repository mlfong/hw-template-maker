'''
makehw.py
@author mlfong
@date aug 2012
'''

class TkGui:
    def __init__(self):
        self.root = Tk()
        self.root.title("LaTeX Homework Maker by mlfong")
        
        format_frame = Frame(self.root)
        format_frame.pack(side="top",expand=True)
        self.format_var = IntVar()
        self.old_format_var = 0
        
        top_frame = Frame(self.root)
        top_frame.pack(side="top",expand=True)

        entry_label_frame = Frame(top_frame)
        entry_label_frame.pack(side="left",expand=False)
        title_label = Label(entry_label_frame, text="Title:", height=2)
        title_label.pack(side="top")
        due_date_label = Label(entry_label_frame, text="Due Date:", height=1)
        due_date_label.pack(side="top")
        class_label = Label(entry_label_frame, text="Class:", height=2)
        class_label.pack(side="top")
        class_time_label = Label(entry_label_frame, text="Class Time:", height=1)
        class_time_label.pack(side="top")
        instructor_label = Label(entry_label_frame, text="Instructor:")
        instructor_label.pack(side="top")
        author_label = Label(entry_label_frame, text="Author:",height=2)
        author_label.pack(side="top")


        entry_frame = Frame(top_frame)
        entry_frame.pack(side="left",expand=True)
        self.title_text_entry = Entry(entry_frame,width=50)
        self.title_text_entry.pack(side="top",expand=True)
        self.title_text_entry.insert(0, "")
        self.due_date_text_entry = Entry(entry_frame,width=50)
        self.due_date_text_entry.pack(side="top",expand=True)
        self.due_date_text_entry.insert(0, "")
        self.class_text_entry = Entry(entry_frame,width=50)
        self.class_text_entry.pack(side="top",expand=True)
        self.class_text_entry.insert(0, "")
        self.class_time_text_entry = Entry(entry_frame,width=50)
        self.class_time_text_entry.pack(side="top",expand=True)
        self.class_time_text_entry.insert(0, "")
        self.instructor_text_entry = Entry(entry_frame,width=50)
        self.instructor_text_entry.pack(side="top",expand=True)
        self.instructor_text_entry.insert(0, "")
        self.author_text_entry = Entry(entry_frame,width=50)
        self.author_text_entry.pack(side="top",expand=True)
        self.author_text_entry.insert(0, "")
        
        button_frame = Frame(top_frame)
        button_frame.pack(side="top", expand=True)
        make_button = Button(button_frame, text="Make LaTeX", command=self.make)
        make_button.pack(side="top")
        self.status = StringVar()
        self.status_label = Label(self.root, textvariable = self.status)
        self.status_label.pack(side='top')
        close_button = Button(button_frame, text="Close", command=self.close)
        close_button.pack(side="top")

    def run(self):
        self.root.mainloop()
    
    def close(self):
        self.root.quit()
    
    def make(self):
        
            
        try:
            title_text = self.title_text_entry.get().replace(' ', '\\ ')
            due_date_text = self.due_date_text_entry.get().replace(' ', '\\ ')
            class_text = self.class_text_entry.get().replace(' ', '\\ ')
            class_time_text = self.class_time_text_entry.get().replace(' ', '\\ ')
            instructor_text = self.instructor_text_entry.get().replace(' ', '\\ ')
            author_text = self.author_text_entry.get().replace(' ', '\\ ')
                        
            s = makeString(title_text, due_date_text, class_text, class_time_text, instructor_text, author_text)
            
            import os.path
            mypath = self.title_text_entry.get().lower().replace(' ', '_')
            if not os.path.isdir(mypath):
               os.makedirs(mypath)
            hw_file = mypath+'/homework.tex'
            
            f = open(hw_file, 'r+') if os.path.exists(hw_file) else open(hw_file, 'w')
            f.write(s)
            f.close()
            self.status.set("Saved to " + hw_file)

        except Exception,err:
            print "Create failed, could not get text."
            self.close()

def makeString(a,b,c,d,e,f):
    s = r'''\documentclass{article}
    % Change "article" to "report" to get rid of page number on title page
    \usepackage{amsmath,amsfonts,amsthm,amssymb}
    \usepackage{setspace}
    \usepackage{Tabbing}
    \usepackage{fancyhdr}
    \usepackage{lastpage}
    \usepackage{extramarks}
    \usepackage{chngpage}
    \usepackage{soul,color}
    \usepackage{graphicx,float,wrapfig}

    % In case you need to adjust margins:
    \topmargin=-0.45in      %
    \evensidemargin=0in     %
    \oddsidemargin=0in      %
    \textwidth=6.5in        %
    \textheight=9.0in       %
    \headsep=0.25in         %

    % Homework Specific Information
    \newcommand{\hmwkTitle}{'''
    s += a
    s +=r'''}
    \newcommand{\hmwkDueDate}{'''
    s += b
    s +=r'''}
    \newcommand{\hmwkClass}{'''
    s += c
    s +=r'''}
    \newcommand{\hmwkClassTime}{'''
    s += d
    s +=r'''}
    \newcommand{\hmwkClassInstructor}{'''
    s += e
    s +=r'''}
    \newcommand{\hmwkAuthorName}{'''
    s += f
    s +=r'''}
    \newcommand{\tab}{\hspace*{0.5in}}
    
    % Setup the header and footer
    \pagestyle{fancy}                                                       %
    \lhead{\hmwkAuthorName}                                                 %
    \chead{\hmwkClass\ (\hmwkClassInstructor\ \hmwkClassTime): \hmwkTitle}  %
    \rhead{\firstxmark}                                                     %
    \lfoot{\lastxmark}                                                      %
    \cfoot{}                                                                %
    \rfoot{Page\ \thepage\ of\ \pageref{LastPage}}                          %
    \renewcommand\headrulewidth{0.4pt}                                      %
    \renewcommand\footrulewidth{0.4pt}                                      %

    % This is used to trace down (pin point) problems
    % in latexing a document:
    %\tracingall

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Some tools
    \newcommand{\enterProblemHeader}[1]{\nobreak\extramarks{#1}{#1 continued on next page\ldots}\nobreak%
                                        \nobreak\extramarks{#1 (continued)}{#1 continued on next page\ldots}\nobreak}%
    \newcommand{\exitProblemHeader}[1]{\nobreak\extramarks{#1 (continued)}{#1 continued on next page\ldots}\nobreak%
                                       \nobreak\extramarks{#1}{}\nobreak}%

    \newlength{\labelLength}
    \newcommand{\labelAnswer}[2]
      {\settowidth{\labelLength}{#1}%
       \addtolength{\labelLength}{0.25in}%
       \changetext{}{-\labelLength}{}{}{}%
       \noindent\fbox{\begin{minipage}[c]{\columnwidth}#2\end{minipage}}%
       \marginpar{\fbox{#1}}%

       % We put the blank space above in order to make sure this
       % \marginpar gets correctly placed.
       \changetext{}{+\labelLength}{}{}{}}%

    \setcounter{secnumdepth}{0}
    \newcommand{\homeworkProblemName}{}%
    \newcounter{homeworkProblemCounter}%
    \newenvironment{homeworkProblem}[1][Problem \arabic{homeworkProblemCounter}]%
      {\stepcounter{homeworkProblemCounter}%
       \renewcommand{\homeworkProblemName}{#1}%
       \section{\homeworkProblemName}%
       \enterProblemHeader{\homeworkProblemName}}%
      {\exitProblemHeader{\homeworkProblemName}}%

    \newcommand{\problemAnswer}[1]
      {\noindent\fbox{\begin{minipage}[c]{\columnwidth}#1\end{minipage}}}%

    \newcommand{\problemLAnswer}[1]
      {\labelAnswer{\homeworkProblemName}{#1}}

    \newcommand{\homeworkSectionName}{}%
    \newlength{\homeworkSectionLabelLength}{}%
    \newenvironment{homeworkSection}[1]%
      {% We put this space here to make sure we're not connected to the above.
       % Otherwise the changetext can do funny things to the other margin

       \renewcommand{\homeworkSectionName}{#1}%
       \settowidth{\homeworkSectionLabelLength}{\homeworkSectionName}%
       \addtolength{\homeworkSectionLabelLength}{0.25in}%
       \changetext{}{-\homeworkSectionLabelLength}{}{}{}%
       \subsection{\homeworkSectionName}%
       \enterProblemHeader{\homeworkProblemName\ [\homeworkSectionName]}}%
      {\enterProblemHeader{\homeworkProblemName}%

       % We put the blank space above in order to make sure this margin
       % change doesn't happen too soon (otherwise \sectionAnswer's can
       % get ugly about their \marginpar placement.
       \changetext{}{+\homeworkSectionLabelLength}{}{}{}}%

    \newcommand{\sectionAnswer}[1]
      {% We put this space here to make sure we're disconnected from the previous
       % passage

       \noindent\fbox{\begin{minipage}[c]{\columnwidth}#1\end{minipage}}%
       \enterProblemHeader{\homeworkProblemName}\exitProblemHeader{\homeworkProblemName}%
       \marginpar{\fbox{\homeworkSectionName}}%

       % We put the blank space above in order to make sure this
       % \marginpar gets correctly placed.
       }%

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Make title
    \title{\vspace{2in}\textmd{\textbf{\hmwkClass:\ \hmwkTitle}}\\\normalsize\vspace{0.1in}\small{Due\ on\ \hmwkDueDate}\\\vspace{0.1in}\large{\textit{\hmwkClassInstructor\ \hmwkClassTime}}\vspace{3in}}
    \date{}
    \author{\textbf{\hmwkAuthorName}}
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    \begin{document}
    \begin{spacing}{1.1}
    \maketitle
    \newpage
    % Uncomment the \tableofcontents and \newpage lines to get a Contents page
    % Uncomment the \setcounter line as well if you do NOT want subsections
    %       listed in Contents
    %\setcounter{tocdepth}{1}
    %\tableofcontents
    %\newpage

    % When problems are long, it may be desirable to put a \newpage or a
    % \clearpage before each homeworkProblem environment

    \clearpage
    \begin{homeworkProblem}
    \end{homeworkProblem}
    
    \problemAnswer{}

    \end{spacing}
    \end{document}

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %----------------------------------------------------------------------%
    % The following is copyright and licensing information for
    % redistribution of this LaTeX source code; it also includes a liability
    % statement. If this source code is not being redistributed to others,
    % it may be omitted. It has no effect on the function of the above code.
    %----------------------------------------------------------------------%
    % Copyright (c) 2007, 2008, 2009, 2010, 2011 by Theodore P. Pavlic
    %
    % Unless otherwise expressly stated, this work is licensed under the
    % Creative Commons Attribution-Noncommercial 3.0 United States License. To
    % view a copy of this license, visit
    % http://creativecommons.org/licenses/by-nc/3.0/us/ or send a letter to
    % Creative Commons, 171 Second Street, Suite 300, San Francisco,
    % California, 94105, USA.
    %
    % THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
    % OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    % MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
    % IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
    % CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
    % TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
    % SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
    %----------------------------------------------------------------------%'''
    
    return s

def usage():
    print 'Homework LaTeX Maker by mlfong'
    print 'Usage:'
    print 'For GUI, use the call'
    print '\tpython makehw.py -g'
    print 'For command line use the call'
    print '\tpython makehw.py TITLE DUE_DATE CLASS CLASS_TIME INSTRUCTOR AUTHOR'

    sys.exit(1)

def main():
    title_text = sys.argv[1].replace(' ', '\\ ')
    due_date_text = sys.argv[2].replace(' ', '\\ ')
    class_text = sys.argv[3].replace(' ', '\\ ')
    class_time_text = sys.argv[4].replace(' ', '\\ ')
    instructor_text = sys.argv[5].replace(' ', '\\ ')
    author_text = sys.argv[6].replace(' ', '\\ ')

    s = makeString(title_text, due_date_text, class_text, class_time_text, instructor_text, author_text)
    
    import os.path
    mypath = sys.argv[1].lower().replace(' ', '_')
    if not os.path.isdir(mypath):
       os.makedirs(mypath)
    hw_file = mypath+'/homework.tex'
    
    f = open(hw_file, 'r+') if os.path.exists(hw_file) else open(hw_file, 'w')
    f.write(s)
    f.close()
    print "Saved to " + hw_file


    #usage()

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2 and sys.argv[1] == "-g":
        try:
            from Tkinter import *
        except ImportError:
            print "GUI failed.  Could not import Tkinter."
        gui = TkGui()
        gui.run()
    elif len(sys.argv) == 7:
        main()
    else:
        usage()








