from selenium import webdriver
import time
import user_data as ud
import random


class Browser:
    def __init__(self, link):
        self.link = link
        self.browser = webdriver.Chrome()
        Browser.goInstagram(self)

    def goInstagram(self):
        self.browser.get(self.link)
        time.sleep(2)
        Browser.login(self)
        Browser.getFollowersFollowed(self)

    def getFollowersFollowed(self):
        self.browser.find_element_by_xpath(
            "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(4)

        Browser.scrollDown(self)
        time.sleep(2)

        followersWeb = self.browser.find_elements_by_class_name(
            "x9f619.xjbqb8w.x1rg5ohu.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x6s0dn4.x1oa3qoh.x1nhvcw1")

        followersList = []
        for follower in followersWeb:
            followersList.append(follower.text)
        time.sleep(3)

        self.browser.get(self.link + "/" + ud.username + "/following")
        time.sleep(5)

        Browser.scrollDown(self)
        time.sleep(2)

        followedWeb = self.browser.find_elements_by_class_name(
            "x9f619.xjbqb8w.x1rg5ohu.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x6s0dn4.x1oa3qoh.x1nhvcw1")
        followedList = []
        for followed in followedWeb:
            followedList.append(followed.text)

        unfollowers = list(set(followedList) - set(followersList))

        with open("unfollewers.txt", "w") as file:
            for unfollower in unfollowers:
                file.write(unfollower + "\n")

    def scrollDown(self):
        jsCommand = """
        page = document.querySelector("._aano");
        page.scrollTo(0, page.scrollHeight);
        var endPage = page.scrollHeight;
        return endPage;
        """
        endPage = self.browser.execute_script(jsCommand)
        while True:
            end = endPage
            time.sleep(2)
            endPage = self.browser.execute_script(jsCommand)
            if endPage == end:
                break
            if endPage < end:
                break

    def login(self):
        username = self.browser.find_element_by_name("username")
        password = self.browser.find_element_by_name("password")

        username.send_keys(ud.username)
        password.send_keys(ud.password)
        time.sleep(5)

        loginBtn = self.browser.find_element_by_css_selector(
            "#loginForm > div > div:nth-child(3) > button > div").click()
        time.sleep(8)

        ###########################################################
        # if you use two-factor authentication, enable the code in this field.
        # verificaitonCodeLink = self.browser.find_element_by_xpath(
        #     "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[4]/button").click()
        # time.sleep(5)
        #
        # randomCode = random.choice(ud.backup_codes)
        # verificationCode = self.browser.find_element_by_name("verificationCode").send_keys(randomCode)
        #
        # confirmBtn = self.browser.find_element_by_class_name("_acan._acap._acas._aj1-").click()
        # time.sleep(8)
        ###########################################################

        self.browser.get(self.link + "/" + ud.username)
        time.sleep(5)
