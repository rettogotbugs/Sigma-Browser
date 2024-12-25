import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit,
    QWidget, QTabWidget, QFileDialog, QMenuBar, QMenu, QAction, QMessageBox, QListWidget, QCompleter
)
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineDownloadItem
from PyQt5.QtCore import QUrl, Qt


class BrowserTab(QWebEngineView):
    def __init__(self, incognito=False):
        super().__init__()
        self.incognito = incognito
        if incognito:
            self.page().profile().setHttpCacheType(self.page().profile().NoCache)
            self.page().profile().setPersistentCookiesPolicy(self.page().profile().NoPersistentCookies)
            print("Incognito Mode Enabled")


class SigmaBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sigma Browser")
        self.setGeometry(100, 100, 1200, 800)

        os.environ["QT_QPA_PLATFORM"] = "xcb"  # For X11 support, change to 'wayland' if using Wayland

        self.bookmarks = []

        # Main Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Tabs
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(lambda _: self.update_url_bar())
        self.layout.addWidget(self.tabs)

        # Navigation Bar
        self.navbar = QHBoxLayout()
        self.layout.addLayout(self.navbar)

        self.back_button = QPushButton("<")
        self.back_button.clicked.connect(self.navigate_back)
        self.navbar.addWidget(self.back_button)

        self.forward_button = QPushButton(">")
        self.forward_button.clicked.connect(self.navigate_forward)
        self.navbar.addWidget(self.forward_button)

        self.refresh_button = QPushButton("⟳")
        self.refresh_button.clicked.connect(self.reload_page)
        self.navbar.addWidget(self.refresh_button)

        self.home_button = QPushButton("🏠 Home")
        self.home_button.clicked.connect(self.navigate_home)
        self.navbar.addWidget(self.home_button)

        self.bookmark_button = QPushButton("🌟 Bookmark")
        self.bookmark_button.clicked.connect(self.add_bookmark)
        self.navbar.addWidget(self.bookmark_button)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.navbar.addWidget(self.url_bar)

        # Search Completer
        self.search_completer = QCompleter(['google.com', 'yahoo.com', 'youtube.com', 'reddit.com'])
        self.url_bar.setCompleter(self.search_completer)

        # Menu Bar
        self.menu_bar = QMenuBar()
        self.setMenuBar(self.menu_bar)

        file_menu = QMenu("File", self)
        self.menu_bar.addMenu(file_menu)

        new_tab_action = QAction("New Tab", self)
        new_tab_action.triggered.connect(self.add_tab)
        file_menu.addAction(new_tab_action)

        new_incognito_action = QAction("New Incognito Tab", self)
        new_incognito_action.triggered.connect(self.add_incognito_tab)
        file_menu.addAction(new_incognito_action)

        save_page_action = QAction("Save Page", self)
        save_page_action.triggered.connect(self.save_page)
        file_menu.addAction(save_page_action)

        show_bookmarks_action = QAction("Show Bookmarks", self)
        show_bookmarks_action.triggered.connect(self.show_bookmarks)
        file_menu.addAction(show_bookmarks_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Start with one tab
        self.add_tab()

    def add_tab(self, incognito=False):
        browser_tab = BrowserTab(incognito)
        browser_tab.setUrl(QUrl("https://www.google.com"))
        browser_tab.urlChanged.connect(lambda url: self.update_url_bar())
        browser_tab.page().profile().downloadRequested.connect(self.handle_download)
        index = self.tabs.addTab(browser_tab, "New Tab")
        self.tabs.setCurrentIndex(index)

    def add_incognito_tab(self):
        QMessageBox.information(self, "Caught in 4K", "Incognito Mode Activated! 🕵️‍♂️💥")
        self.add_tab(incognito=True)

    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)

    def navigate_home(self):
        self.tabs.currentWidget().setUrl(QUrl("https://www.mosambika.com"))  # Fun homepage with juice theme

    def navigate_back(self):
        self.tabs.currentWidget().back()

    def navigate_forward(self):
        self.tabs.currentWidget().forward()

    def reload_page(self):
        self.tabs.currentWidget().reload()

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.tabs.currentWidget().setUrl(QUrl(url))

    def update_url_bar(self):
        current_tab = self.tabs.currentWidget()
        if current_tab:
            url = current_tab.url()
            self.url_bar.setText(url.toString())
            self.tabs.setTabText(self.tabs.currentIndex(), url.toString().split("://")[1].split("/")[0])

    def save_page(self):
        current_tab = self.tabs.currentWidget()
        if current_tab:
            filename, _ = QFileDialog.getSaveFileName(self, "Save Page As", "", "HTML Files (*.html);;All Files (*)")
            if filename:
                current_tab.page().save(filename, current_tab.page().CompleteHtmlSaveFormat)

    def add_bookmark(self):
        current_tab = self.tabs.currentWidget()
        if current_tab:
            url = current_tab.url().toString()
            self.bookmarks.append(url)
            QMessageBox.information(self, "Bookmark Added", f"Bookmarked: {url}")

    def show_bookmarks(self):
        bookmark_window = QWidget()
        bookmark_window.setWindowTitle("Bookmarks")
        bookmark_window.setGeometry(150, 150, 400, 300)

        layout = QVBoxLayout()
        bookmark_window.setLayout(layout)

        bookmark_list = QListWidget()
        bookmark_list.addItems(self.bookmarks)
        layout.addWidget(bookmark_list)

        bookmark_window.show()

    def handle_download(self, download_item: QWebEngineDownloadItem):
        path, _ = QFileDialog.getSaveFileName(self, "Save File", download_item.suggestedFileName())
        if path:
            download_item.setPath(path)
            download_item.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Sigma Browser")
    window = SigmaBrowser()
    window.show()
    sys.exit(app.exec_())
