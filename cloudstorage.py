import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A6yzz_VKnVvAJ30z3jEWV-3UnmNHHEk04ENOEZzP5vQP1XMOmY9sxyPlTaZoY8Vxfs6YNx6Vh2-qigciJlSmNLqv_nxQaa2NwePWSW2aOrmlIbDjudBnQJMUIP3zVmKH1Dpokmc'
    transferData = TransferData(access_token)

    file_from = 'D:/Coding folders/Python/Classes projects  97-107/Project 101/text.txt'
    file_to = '/Project--101/text.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved")
main()