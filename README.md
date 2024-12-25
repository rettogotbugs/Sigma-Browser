# Sigma-Browser
A python based browser only for sigmas
--------------------------------------------------------------

Sigma Browser is a modern and feature-rich web browser built using PyQt5 and Python. It includes essential browser features like tab management, incognito mode, bookmarks, file downloads, and a custom homepage, all wrapped in a playful and interactive user interface. The browser is designed for users who want both functionality and a fun browsing experience.
Features

    Multiple Tabs: Open multiple tabs with ease. Each tab can load any website you like.
    Incognito Mode: Browse privately with the incognito mode. No history or cookies are saved. You’ll also get a funny "Caught in 4K" pop-up message.
    Bookmarks: Save your favorite websites as bookmarks and view them anytime.
    File Downloading: Download files from websites with an intuitive prompt to choose where to save the file.
    Custom Homepage: A fun and interactive homepage with a search bar and personalized welcome message.
    Navigation Controls: Back, forward, refresh, and home buttons for easy navigation.

Installation

To run Sigma Browser locally, you need to have Python installed on your system. Follow these steps:
Step 1: Clone the Repository

git clone https://github.com/your-username/sigma-browser.git
cd sigma-browser

Step 2: Install Dependencies

Sigma Browser uses PyQt5 for its GUI components and web engine. Install the required dependencies using pip.

pip install PyQt5
pip install PyQtWebEngine

Step 3: Run the Application

After installing the dependencies, you can run the Sigma Browser application by executing the following command:

python sigma_browser.py

Code Explanation

The Sigma Browser code is structured into the following main components:

    SigmaBrowser Class: This is the main window of the browser. It handles tab creation, navigation buttons, and the overall layout.
    Incognito Mode: The add_incognito_tab function creates new tabs in incognito mode with no cache or cookies.
    Bookmarks: The browser allows users to add bookmarks and view them in a separate window.
    Custom Homepage: A personalized HTML page loads by default when the browser starts, featuring a search bar and interactive elements.

Contributing

Contributions to the Sigma Browser project are welcome! If you'd like to improve the browser or add new features, please fork the repository and submit a pull request.
How to Contribute

    Fork the repository.
    Create a new branch (git checkout -b feature/your-feature).
    Commit your changes (git commit -am 'Add new feature').
    Push to the branch (git push origin feature/your-feature).
    Open a pull request.

License

This project is open-source and licensed under the MIT License.
