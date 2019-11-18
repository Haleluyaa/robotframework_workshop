import requests
import urllib.parse
__version__ = '0.0.1'

class LineNoti():

    def __init__(self):
        ROBOT_LIBRARY_SCOPE = 'GLOBAL'
        ROBOT_LIBRARY_VERSION = __version__
        self.URL_LINE = 'https://notify-api.line.me/api/notify'

    def set_line_token(self,line_token):
        """
        Arguments:
        | line_token      |  An access token for authentication  |

        Example:

        | *Keywords*           |  *line_token*                                      |
        | Set Line Token           |  OHe8Yzjhy6X9LWv3jeJH4HhBvpGoR5KjRMG6BzUX1v0 |

        """
        self.LINE_ACCESS_TOKEN = line_token

    def line_text(self,message):
        """
        Arguments:
        |   message     |  	1000 characters max  |

        Example:

        | *Keywords*           |  *message*                                      |
        | Line Text          |  Test Message  |

        """
        msg = urllib.parse.urlencode({"message":message})
        LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+self.LINE_ACCESS_TOKEN}
        session = requests.Session()
        session_post = session.post(self.URL_LINE, headers=LINE_HEADERS, data=msg)
        print(session_post.text)

    def line_pic(self,path_file):
        """
        Arguments:
        |   path_file     |  Upload a image file to the LINE server.Supported image format is png and jpeg. |

        Example:

        | *Keywords*           |  *path_file*                                      |
        | Line Pic          |  *D://testCode.png*  |

        """
        file_img = {'imageFile': open(path_file, 'rb')}
        msg = ({'message': ' '})
        LINE_HEADERS = {"Authorization":"Bearer "+self.LINE_ACCESS_TOKEN}
        session = requests.Session()
        session_post = session.post(self.URL_LINE, headers=LINE_HEADERS, files=file_img, data=msg)
        print(session_post.text)

    def line_pic_url(self,url):
        """
        Arguments:
        |   path_file     |  Upload a image file to the LINE server.Supported image format is png and jpeg. |

        Example:

        | *Keywords*           |  *Parameters*                                      |
        | Line Pic URL         |  *https://i2.wp.com/metro.co.uk/wp-content/uploads/2019/03/SEC_57712924.jpg?quality=90&strip=all&zoom=1&resize=644%2C338&ssl=1* |

        """
        msg = ({'message': ' ','imageThumbnail': url,'imageFullsize': url})
        LINE_HEADERS = {"Authorization":"Bearer "+self.LINE_ACCESS_TOKEN}
        session = requests.Session()
        session_post = session.post(self.URL_LINE, headers=LINE_HEADERS, data=msg)
        print(session_post.text)

    def line_sticker(self,PackageId,StickerId):
        """
        Arguments:
        |   PackageId     |  https://devdocs.line.me/files/sticker_list.pdf |
        |   StickerId     |  https://devdocs.line.me/files/sticker_list.pdf |

        Example:

        | *Keywords*           |  *Parameters* | *Parameters* |
        | Line Sticker         |  1  |  1  |

        """
        msg = ({'message': ' ','stickerPackageId': PackageId,'stickerId': StickerId})
        LINE_HEADERS = {"Authorization":"Bearer "+self.LINE_ACCESS_TOKEN}
        session = requests.Session()
        session_post = session.post(self.URL_LINE, headers=LINE_HEADERS, data=msg)
        print(session_post.text)