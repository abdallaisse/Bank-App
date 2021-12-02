# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 23:50:29 2020

@author: abdil
"""

import sqlite3
import time
import random
import sys
from datetime import date, timedelta
from contextlib import closing

db_file = "accounts.db"
conn = sqlite3.connect(db_file)
c = conn.cursor()

# c.execute("""CREATE TABLE user_accounts(
#                acc_no interger NOT NULL,
#                open_date interger NOT NULL,
#                first_name text NOT NULL,
#                last_name text NOT NULL,
#                user_name text NOT NULL,
#                password interger NOT NULL,
#                acc_balance real NOT NULL
#                )""")


def display_menu():
    print("\n|----------DOMA BANK----------|\n")
    print("MAIN MENU\n")
    print("1. Open an Account")
    print("2. Signing in your Account")
    print("3. Logout")
    print()


def open_account():
    while True:
        try:

            print("Open a Bank Account\n")
            try:
                open_date = time.ctime()
                first_name = str(input("First Name:\t"))
                last_name = str(input("Last Name:\t"))
                user_name = str(
                    input("Please Choose a unique username and Enter it:\t"))
                password = int(input("Please Enter a unique password:\t"))
                acc_no = random.randint(1000000, 9999999)
            except ValueError:
                print("Invalid Entry.\n")
                break
            except Exception as e:
                print("Error: %s" % e)
                break
            print("\n")
            acc_balance = 0.00

            def open_in_database():
                with closing(conn.cursor()) as c:
                    sql = '''INSERT INTO user_accounts (open_date,acc_no,first_name,last_name,
                    user_name,password,acc_balance) 
                    VALUES (?,?, ?, ?, ?, ?, ?)'''
                    c.execute(sql, (open_date, acc_no, first_name,
                              last_name, user_name, password, acc_balance))
                    conn.commit()
                    print("|----------DOMA BANK----------|\n")
                    print("Successful!! "+first_name +
                          ", You Have an Account with us now\n")
                    print("New Account Info:\n")
                    print("Full Name:\t"+first_name+" " + last_name)
                    print("Account Number:\t", acc_no)
                    print("User Name:\t"+user_name)
                    print("Password:\t", password, "\n")
                    print("Account Balance:\t", acc_balance, "\n")
                    print("Conguratulations "+first_name)
            open_in_database()
            display_menu()
            break
        except ValueError:
            print("Invalid Entry.\n")
            break
        except Exception as e:
            print("Error: %s" % e)
            break


def signing_menu():
    print("|----------DOMA BANK----------|\n")
    print("MENU\n")
    print("1. Account Balance")
    print("2. Make a Deposit")
    print("3. Withdraw Money from your Account")
    print("4. Transfer Money")
    print("5. Logout\n")


def show_balance():
    print("Account Balance\n")
    while True:
        try:
            print("Please Signing to your Account\n")
            acc_no = int(input("Please Enter your Account Number:\t"))
            pass_word = int(input("Please Enter your Password:\t"))
            print("\n")
            c.execute(
                "SELECT * FROM user_accounts WHERE acc_no = ? AND password = ?", (acc_no, pass_word))
            account = c.fetchone()
            if acc_no and pass_word in account:
                print("|----------DOMA BANK----------|\n")
                print(time.ctime(), "\n")
                print('Hello\t' + account[2])
                print("Account No:\t", account[0])
                print("Account Balance:\t", account[6])
                print("\tThank you and Goodbye {}\n".format(account[2]))
                print("|----------END OF TRANSACTION-----------|\n")
            else:
                print("You Entered a wrong account Number Or Password")
                break
                acc_signing()
        except ValueError:
            print("Invalid Entry.\n")
            break
        except Exception as e:
            print("Error: %s" % e)
            break
        conn.commit()
        acc_signing()
        break


def deposit():
    transaction = "Deposit"
    print("Money Deposit\n")
    while True:
        try:
            print("Please Signing to your Account\n")
            acc_no = int(input("Please Enter your Account Number:\t"))
            pass_word = int(input("Please Enter your Password:\t"))
            print("\n")
            c.execute(
                "SELECT * FROM user_accounts WHERE acc_no = ? AND password = ?", (acc_no, pass_word))
            account = c.fetchone()
            if acc_no and pass_word in account:
                print('Hello\t' + account[2])
                deposit_m = float(
                    input("How Much do you want to deposit today:\t"))
                if deposit_m <= 0:
                    print("Invalid Entry!!!")
                    break
                print("\n")
                new_balance = account[6] + deposit_m
                c.execute(
                    "UPDATE user_accounts SET acc_balance = ? WHERE acc_no = ?", (new_balance, acc_no,))
                conn.commit()
                print("|----------DOMA BANK----------|\n")
                print("\t\tReceipt\n")
                print(time.ctime(), "\n")
                print("Account No:\t", account[0])
                print("Transaction:\t" + transaction)
                print("Amount Deposited:\t", deposit_m)
                print("Account Balance:\t", new_balance, "\n")
                print("\tThank you and Goodbye {}\n".format(account[2]))
                print("|----------END OF TRANSACTION-----------|\n")
                conn.commit()
            else:
                print("You Entered a wrong account Number Or Password")
                acc_signing()
        except ValueError:
            print("Invalid Entry.\n")
            break
        except Exception as e:
            print("Error: %s" % e)
            break
        conn.commit()
        acc_signing()
        break


def withdraw():
    while True:
        transaction = "Withdrawal"
        print("Money Withdrawal\n")
        try:
            print("Please Signing to your Account\n")
            acc_no = int(input("Please Enter your Account Number:\t"))
            pass_word = int(input("Please Enter your Password:\t"))
            print("\n")
            c.execute(
                "SELECT * FROM user_accounts WHERE acc_no = ? AND password = ?", (acc_no, pass_word))
            account = c.fetchone()
            if acc_no and pass_word in account:
                print('Hello\t' + account[2])
                withdraw_m = float(
                    input("How Much do you want to withdraw today:\t"))
                if account[6] <= 0 or withdraw_m > account[6]:
                    print("You dont have enough money at your  account!!!")
                    break
                print("\n")
                new_balance = account[6] - withdraw_m
                c.execute(
                    "UPDATE user_accounts SET acc_balance = ? WHERE acc_no = ?", (new_balance, acc_no,))
                print("|----------DOMA BANK----------|\n")
                print("\t\tReceipt\n")
                print(time.ctime(), "\n")
                print("Account No:\t", account[0])
                print("Transaction: " + transaction)
                print("Amount Withdrawn:\t", withdraw_m)
                print("Account Balance:\t", new_balance, "\n")
                print("\tThank you and Goodbye {}\n".format(account[2]))
                print("|----------END OF TRANSACTION-----------|\n")
                conn.commit()
            else:
                print("You Entered a wrong account Number Or Password")
                acc_signing()
        except ValueError:
            print("Invalid Entry.\n")
            break
        except Exception as e:
            print("Error: %s" % e)
            break
        conn.commit()
        acc_signing()
        break


def transfer():
    while True:
        transaction = "Transfer"
        print("Money Transfer\n")
        try:
            print("Please Signing to your Account\n")
            acc_no = int(input("Please Enter your Account Number:\t"))
            pass_word = int(input("Please Enter your Password:\t"))
            print("\n")
            c.execute(
                "SELECT * FROM user_accounts WHERE acc_no = ? AND password = ?", (acc_no, pass_word))
            account = c.fetchone()
            if acc_no and pass_word in account:
                print('Hello\t' + account[2])
                transfer_to = int(input("Transfer Account Number:\t"))
                c.execute(
                    "SELECT * FROM user_accounts WHERE acc_no = ?", (transfer_to,))
                trans_acc = c.fetchone()
                try:
                    if transfer_to in trans_acc:
                        transfer_m = float(
                            input("How Much do you want to Transfer today:\t"))
                        if account[6] <= 0 or transfer_m > account[6]:
                            print("You dont have enough money at your  account!!!")
                            break
                        print("\n")
                        new_balance = account[6] - transfer_m
                        trans_to_balance = trans_acc[7] + transfer_m
                        c.execute(
                            "UPDATE user_accounts SET acc_balance = ? WHERE acc_no = ?", (new_balance, acc_no,))
                        conn.commit()
                        c.execute("UPDATE user_accounts SET acc_balance = ? WHERE acc_no = ?",
                                  (trans_to_balance, transfer_to,))
                        conn.commit()
                        print("|----------DOMA BANK----------|\n")
                        print("\t\tReceipt\n")
                        print(time.ctime(), "\n")
                        print("Account No:\t", account[0])
                        print("Transaction: " + transaction)
                        print("Account Tranferred to:\t", trans_acc[0])
                        print("Transferred to:\t",
                              trans_acc[2], " ", trans_acc[3])
                        print("Amount Transfered:\t", transfer_m)
                        print("Account Balance:\t", new_balance, "\n")
                        print(
                            "\tThank you and Goodbye {}\n".format(account[2]))
                        print("|----------END OF TRANSACTION-----------|\n")
                        conn.commit()
                    else:
                        print("You Entered a wrong account Number")
                        transfer()
                except ValueError:
                    print("Invalid Entry.\n")
                    break
                except Exception as e:
                    print("Error: %s" % e)
                    break
            else:
                print("You Entered a wrong account Number Or Password")
                acc_signing()
        except ValueError:
            print("Invalid Entry.\n")
            break
        except Exception as e:
            print("Error: %s" % e)
            break
        conn.commit()
        acc_signing()
        break


def acc_signing():
    global acc_no, pass_word, account
    print("Signing in your Account\n")
    while True:
        try:
            signing_menu()
            user_input = input("Please Choose from the Menu:\t")
            if user_input == "1":
                show_balance()
            elif user_input == "2":
                deposit()
            elif user_input == "3":
                withdraw()
            elif user_input == "4":
                transfer()
            elif user_input == "5":
                sys.exit()
            else:
                print("Not a valid command. Please try again.\n")
                acc_signing()
        except ValueError:
            print("Invalid Entry.\n")
            break
        except Exception as e:
            print("Error: %s" % e)
            break


def main():
    display_menu()
    while True:
        try:

            userinput = input("Please Choose from the Main Menu:\t")
            if userinput == "1":
                open_account()
            elif userinput == "2":
                acc_signing()
            elif userinput == "3":
                print("Good Bye!")
                time.sleep(2)
                break
            else:
                print("Not a valid command. Please try again.\n")
        except ValueError:
            print("Invalid Entry.\n")
            time.sleep(3)
            break
        except Exception as e:
            print("Error: %s" % e)
            time.sleep(3)
            break


if __name__ == "__main__":
    main()


conn.commit()
conn.close()
