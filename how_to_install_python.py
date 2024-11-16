# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:49:29 2024

Author: Oscar Palmgren
© Oscar Palmgren 2024. All rights reserved.
"""

import streamlit as st

st.set_page_config("How to install Python?", '🐍')

st.title("The ophidiophobe's guide to get started with Python")
st.markdown('''
            Python is a versatile programming language known for its ease of use.
            It's widely used in scientific computing, data analysis, artificial intelligence, and more thanks to its extensive library of third-party extensions.
            Python emphasizes simplicity, productivity and community engagement, making it a popular choice for both beginner and experienced programmers.
            Let's get you started by walking through the installation process for the programming language and its most popular interactive development environments (IDE).
            We'll incidentally also touch upon installing some common third-party extensions so that you can extend the functionality of Python according to your needs.
            ''')

#---

st.header("Installing Python")

st.subheader("Step 1: Download the installer")
st.video('1 Download Python installer.mp4', loop = True, autoplay = True, muted = True)
st.markdown('''
            Navigate to the official website for the [Python Software Foundation](https://www.python.org/).
            Hover over *Downloads*, the lastest release for Windows will be displayed.
            Click the button for the latest release, the download of the installer will begin.
            ''')
st.warning('''
           **Does your PC already have Python installed?**
           
           To check, open Windows PowerShell and run the command "*python --version*".
           ''', icon = '⚠️')

st.subheader("Step 2: Execute the installer")
st.markdown('''
            Navigate to your downloads folder.
            Locate the installer and run it.
            The installation window pops up.
            ''')

st.subheader("Step 3: Set installation parameters")
st.video('3 Run Python installer.mp4', loop = True, autoplay = True, muted = True)
st.markdown('''
            Check the box for *Add python.exe to PATH*.
            Doing this means your PC will be configured to recognize Python's executable file from any command line interface without needing to specify its full directory path.
            This makes it easier to run an IDE from Windows PowerShell which will come in handy.
            ''')
st.warning('''
           **Have you had Python installed previously?**
           
           If you've previously had Python istalled on your PC, it might already have been added to the system path. To avoid complications from having redundant installations written to the path, do this:

           1. Navigate to *Settings*.
           2. In the search bar, write "*Edit the system environment variables*" and execute the search. The *System Properties* window pops up.
           3. Click the *Environment Variables...* button. The *Environment Variables* window pops up.
           4. Locate the path of the previous Python installation under *User Variables*.
           5. Select the path and click the *Delete* button.
           
           You have now removed the previous installation of Python from your system path, and are ready to proceed with the installation.
           ''', icon = '⚠️')
st.markdown('''
            Also, check the box for *Use admin privileges when installing py.exe* if applicable.
            ''')

st.subheader("Step 4: Finish the installation")
st.video('4 Finish Python installation.mp4', loop = True, autoplay = True, muted = True)
st.markdown('''
            Let the installation run its course.
            Once finished, your PC should be able to recognize the programming language.
            The final dialog window has some useful links to get you familiarized with Python and its syntax.
            ''')
st.success('''
           **Pro tip: Verify the installation!**
           
           To verify, open Windows PowerShell and run the command "*python --version*".
           ''', icon = '✅')
st.markdown('''
            Congratulations on successfully installing Python on your PC! 🎉
            But what's next?
            Simply having the language installed isn't enough to make the most out of it.
            ''')

#---

st.header("Installing an IDE")
st.markdown('''
            While you can write Python code in any text editor, using an Integrated Development Environment (IDE) can make coding easier and more efficient.
            An IDE is a software application that offers tools like a code editor, debugger, and build automation, all in one interface.
            There are many IDEs for Python because they cater to different needs and preferences.
            
            While any IDE (such as PyCharm, Visual Studio Code, or Sublime Text) can be used for general Python coding, some are specialized for scientific computing and data analysis.
            Spyder and the Jupyter Project's offerings, for example, provide tools for interactive computing, data visualization, and integration with scientific libraries.
            In the next steps, we walk you through the process of installing Spyder and Jupyter Notebook to make sure you get to use Python comfortably.
            ''')

st.header("🕸️ Spyder")
st.markdown('''
            Spyder (Scientific PYthon Development EnviRonment) is an open-source IDE specifically designed for scientific and engineering applications.
            It combines powerful editing, analysis, debugging, and profiling functionality within a simple interface.
            Spyder integrates seamlessly with popular libraries for data analysis and visualization like NumPy, SciPy, Pandas, and Matplotlib, as well as machine learning libraries such as TensorFlow and PyTorch, making it an excellent choice in science and research.
            ''')

st.subheader("Step 1: Download the installer")
st.video('1 Download Spyder installer.mp4', loop = True, autoplay = True, muted = True)
st.markdown('''
            Navigate to the [Spyder IDE](https://www.spyder-ide.org/) official website.
            On the landing page, the lastest release for Windows will be displayed.
            Click the button for the latest release, the download of the installer will begin.
            ''')

st.subheader("Step 2: Execute the installer")
st.markdown('''
            Navigate to your downloads folder.
            Locate the installer and run it, the installation window pops up.
            ''')

st.subheader("Step 3: Finish the installation")
st.video('3 Run Spyder installer.mp4', loop = True, autoplay = True, muted = True)
st.markdown('''
            Let the installation run its course.
            Once finished, you should have Spyder installed on your PC.
            Congratulations on installing your first IDE. 🎈
            Now you're ready to start your coding journey in Python!
            ''')
st.markdown('''
            As mentioned, there are many IDEs to chose from.
            Next we'll walk you though the steps of installing Jupyter Notebook, a powerful alternative to Spyder.
            Incidentally, this procedure also touches on the method we use to install third-party extensions in Python.
            ''')
#---

st.header("🪐 Jupyter")
st.markdown('''
            Jupyter Notebook is an open-source web application that allows you to create and share documents containing live code, equations, visualizations, and narrative text.
            It also has the ability to integrate with numerous libraries for data analysis and visualization such as NumPy, SciPy, Pandas, and Matplotlib, as well as machine learning libraries such as TensorFlow and PyTorch.
            Although widely used in scientific research, Jupyter Notebook really shines in education applications thanks to its interactive and integrative format!
            ''')
st.markdown('''
            Jupyter Lab offers an integrated development environment for working with notebooks, code, and data.
            It provides a more flexible and powerful user experience compared to Jupyter Notebook, featuring drag-and-drop functionality, multiple document support, and a customizable workspace.
            ''')

st.subheader("Step 1: Open Windows PowerShell")
st.markdown('''
            To install Jupyter Notebook or Jupyter Lab, you'll need to use Windows PowerShell.
            It's therefore essential you've added the Python installation location to your system path during the Python installation.
            Python uses the "Python Package Index" (PIP) to install most third-party extensions.
            You can use PIP to install Jupyter Notebook, and the process is nearly identical for installing Jupyter Lab.
            ''')

st.subheader("Step 2: Run the installation command")
st.video('2 Install Jupyter Notebook.mp4', loop = True, autoplay = True, muted = True)
st.markdown('''
            On the command line, enter "*pip install notebook*" and hit return.
            The installation should begin promptly.
            ''')
st.success('''
           **Pro tip: Also instal Jupyter Lab!**
           
           Would you also like to install Jupyter Lab, the procedure is almost identical.
           On the command line, enter "*pip install jupyterlab*" and hit return.
           ''', icon = '✅')

st.subheader("Step 3: Launch Jupyter Notebook")
st.video('3 Launch Jupyter Notebook.mp4', loop = True, autoplay = True, muted = True)
st.markdown('''
            You can also lauch Jupyter Notebook directly from within Windows PowerShell.
            On the command line, enter "*jupyter notebook*" and hit return.
            An instance of your notebook environment should be booted up in your default browser.
            ''')
st.success('''
           **Pro tip: Install third-party extensions!**
           
           There are many third-party extensions which expand the functionality of Python.
           You can easily install any of these by calling the "*pip install [...]*" command within Windows PowerShell.
           ''', icon = '✅')
st.markdown('''
            Note that this process will not install any shortcut to Jupyter Notebook and/or Jupyter Lab on your PC. 
            Instead, you can launch the IDEs from within Windows PowerShell at any time.
            Visit the official website for the [Jupyter Project](https://www.jupyter.org/) to read more about Jupyter Notebook and Jupyter Lab.
            ''')
st.markdown('''
            A final congratulations on successfully installing your second (and possibly third) IDE! 🎊
            You now have several powerful tools at your disposal for tackling science and engineering projects or sharing your knowledge with students.
            Your next task is to get comfortable with Python and its syntax, as well as the development environments you've installed.
            Take some time to explore their features and capabilities to make the most out of these powerful resources.
            **Happy coding!**
            ''')

st.divider()
st.markdown(''':grey[
            This guide was written by Oscar Palmgren.
            © Oscar Palmgren 2024. All rights reserved.
            ]''')