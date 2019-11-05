from actors.asker import Asker
from pom.asker.sign_up_page import SignUp
from pom.asker.home_page import HomePage

if __name__ == '__main__':

    asker = Asker()
    # sign_up_page = SignUp(asker)
    # sign_up_page.sign_up(email='testSelenium1@gmail.com', password='MotConVit123!@')
    home_page = HomePage(asker)
    home_page.test()
