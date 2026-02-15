"""Page object for Upload and Download page."""
from pages.base_page import BasePage
from playwright.sync_api import Page
import os


class UploadDownloadPage(BasePage):
    """Page object for DemoQA Upload and Download page."""
    
    # Page URL
    PAGE_URL = "/upload-download"
    
    # Locators
    DOWNLOAD_BUTTON = "#downloadButton"
    UPLOAD_FILE_INPUT = "#uploadFile"
    UPLOADED_FILE_PATH = "#uploadedFilePath"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    def navigate_to_page(self):
        """Navigate to Upload and Download page."""
        self.navigate(self.PAGE_URL)
    
    def click_download_button(self):
        """Click download button."""
        self.logger.info("Clicking download button")
        self.click(self.DOWNLOAD_BUTTON)
    
    def download_file(self, download_path: str = None) -> str:
        """Download file and return the path."""
        self.logger.info("Starting file download")
        
        # Start waiting for download before clicking
        with self.page.expect_download() as download_info:
            self.click_download_button()
        
        download = download_info.value
        
        # Save to specific path if provided
        if download_path:
            file_path = os.path.join(download_path, download.suggested_filename)
            download.save_as(file_path)
            self.logger.info(f"File downloaded to: {file_path}")
            return file_path
        else:
            # Use default download path
            file_path = download.path()
            self.logger.info(f"File downloaded to: {file_path}")
            return file_path
    
    def upload_file(self, file_path: str):
        """Upload a file."""
        self.logger.info(f"Uploading file: {file_path}")
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        self.upload_file(self.UPLOAD_FILE_INPUT, file_path)
    
    def get_uploaded_file_path(self) -> str:
        """Get the uploaded file path text."""
        self.wait_for_element_visible(self.UPLOADED_FILE_PATH, timeout=5000)
        return self.get_text(self.UPLOADED_FILE_PATH)
    
    def get_uploaded_file_name(self) -> str:
        """Get just the file name from uploaded file path."""
        full_path = self.get_uploaded_file_path()
        # Extract filename from "C:\fakepath\filename.ext"
        if full_path:
            return full_path.split("\\")[-1]
        return ""
    
    def is_upload_successful(self) -> bool:
        """Check if file upload was successful."""
        return self.is_visible(self.UPLOADED_FILE_PATH, timeout=5000)
