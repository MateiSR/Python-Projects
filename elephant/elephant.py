from tkinter import *
from tkinter.ttk import *
from newsapi import NewsApiClient
from pytz import timezone
import json, datetime, time, tk, requests, threading
import ctypes

# Get time (RO)
date = datetime.datetime
tz_RO = timezone('Europe/Bucharest')
now = date.now(tz_RO)
current_time = now.strftime("%H:%M")
start_str = date = now.strftime('%d-%m-%Y')
startt = datetime.datetime.strptime(start_str, "%d-%m-%Y")
date_list = [startt + datetime.timedelta(days=x) for x in range(30)]
# List of dates for combobox options
date_list_str = []
for i in date_list:
    j = i.strftime('%d-%m-%Y')
    date_list_str.append(j)
# F: Write json
def write_json(file):
    global reminders
    with open(file, 'w') as outfile:
        json.dump(reminders, outfile)
# F: Read json
def read_json(file):
    global reminders
    with open(file) as json_file:
        reminders = json.load(json_file)

# Read main reminders dictionary
read_json('reminders.json')

# Submit button action (dump to json)
def submit():
    #submit_btn.configure(text='Success!', state=DISABLED)
    reminder_text = reminder.get()
    date_text = date.get()
    time_text = time_entry.get()
    desc_text = desc.get()
    full_text = date_text + ' ' + time_text
    full_datetime = datetime.datetime.strptime(full_text, "%d-%m-%Y %H:%M")
    full_epoch = (full_datetime - datetime.datetime(1970,1,1)).total_seconds()  - 3600 * 3
    reminders[reminder_text] = {}
    reminders[reminder_text]['datetime_text'] = full_text
    reminders[reminder_text]['epoch'] = full_epoch
    reminders[reminder_text]['desc'] = desc_text
    write_json('reminders.json')
    print(f'Reminder \'{reminder_text}\' succesfully added!')

# Check if reminder has expired
def check_active(reminder):
    global reminders
    current_epoch = time.time()
    reminder_epoch = reminders[reminder]['epoch']
    if int(reminder_epoch) < int(current_epoch):
        return False
    else:
        return True

# Check for expired reminders on start
def check_start():
    global reminders
    exp_list = []
    expired = False
    startwin = Tk()
    startwin.iconbitmap('elephant.ico')
    startwin.title('Elephant - Reminder updates')
    startwin.geometry('320x320')
    startwin_t = Text(startwin, height=18, width=35, padx=10, pady=10, wrap=WORD)
    startwin.resizable(0,0)
    title_t = 'Reminder updates'
    startwin_t.insert(END, title_t+'\n')
    startwin_t.tag_add('title_t', '1.0', '1.end')
    startwin_t.tag_config('title_t', font='roboto 16 underline')
    startwin_t.tag_add('added_text', '1.0', '1.end')
    startwin_t.tag_config('added_text', font='roboto 16')
    startwin_t.insert(END, 'Note: Expired reminders will be deleted\n')
    for reminder in reminders:
        if check_active(reminder) == False:
            c_datetime2 = reminders[reminder]['datetime_text']
            c_desc2 = reminders[reminder]['desc']
            added_text = f'- {reminder} [{c_desc2}] expired while you were offline ({c_datetime2})'
            startwin_t.insert(END, added_text+'\n')
            expired = True
            exp_list.append(reminder)
    if expired != True:
        startwin_t.insert(END, f'No reminders expired while you were offline')
    startwin_t.config(state=DISABLED)
    startwin_t.pack()
    for exp in exp_list:
        del(reminders[exp])
    write_json('reminders.json')

# View a list of all reminders (View button)
def view_reminders():
    view = Tk()
    view.iconbitmap('elephant.ico')
    view.title('Elephant - View reminders')
    view.geometry('300x330')
    view.resizable(0,0)
    view.configure(bg='white')
    view_t = Text(view, height=1.5, width=15, wrap=WORD)
    viewt_t = 'Reminders'
    view_t.insert(END, viewt_t+'\n')
    view_t.tag_add('viewt_t', '1.0', '1.end')
    view_t.tag_config('viewt_t', font='roboto 16 underline')
    view_l = Listbox(view, width=38, height=15)
    for reminder in reminders:
        c_datetime = reminders[reminder]['datetime_text']
        view_l.insert(END, f'{reminder} - {c_datetime}\n')
    view_l.activate(0)
    def del_sel():
        sel = view_l.get(ACTIVE)
        cursel = view_l.curselection()
        i = 0
        for key in reminders:
            if i == cursel[0]:
                sel_key = key
            i += 1
        del(reminders[sel_key])
        write_json('reminders.json')
        view_l.delete(ACTIVE)

    del_btn = Button(view, text='Delete', command = del_sel)
    del_btn.place(x=1, y=1)
    view_t.pack()
    view_l.pack()
    del_btn.pack()

# Get news titles
titles = []
def get_titles(top_headlines):
    global titles
    for art in top_headlines['articles']:
        titles.append(art['title'])

# Show News & Stats Window (News button)
def show_news():
    counter_1 = 0
    global titles
    news = Tk()
    news.iconbitmap('elephant.ico')
    news.title('Elephant - News')
    news.geometry('320x380')
    news.resizable(0,0)
    news_t = Text(news, height=15, width=35, wrap=WORD)
    newst_t = 'News'
    news_t.insert(END, newst_t+'\n')
    news_t.tag_add('newst_t', '1.0', '1.end')
    news_t.tag_config('newst_t', font='roboto 16 underline')
    get_titles(top_headlines)
    for title in titles:
        news_t.insert(END, '- '+title+'\n')
        counter_1 += 1
        if counter_1 == 7:
            break
    stats_t = Text(news, height=7, width=35, wrap=WORD)
    statst_t = 'Stats'
    stats_t.insert(END, statst_t+'\n')
    stats_t.tag_add('statst_t', '1.0', '1.end')
    stats_t.tag_config('statst_t', font='roboto 16 underline')
    r = requests.get('https://api.covid19api.com/summary')
    r_data = json.loads(r.text)
    covid_total = r_data['Global']['TotalConfirmed']
    covid_deaths = r_data['Global']['TotalDeaths']
    covid_recovered = r_data['Global']['TotalRecovered']
    stats_t.insert(END, 'Total Confirmed: '+str(covid_total)+'\n')
    stats_t.insert(END, 'Total Recovered: '+str(covid_deaths)+'\n')
    stats_t.insert(END, 'Total Deaths: '+str(covid_recovered)+'\n')
    news_t.config(state=DISABLED)
    stats_t.config(state=DISABLED)
    news_t.pack()
    stats_t.pack()


# F: Thread / Check if reminder finished
alert_active = False
def check_timer():
    global reminders
    global alert_active
    if alert_active != True:
        for reminder in reminders:
            if check_active(reminder) == False:
                exp_rem = reminder
                rem_datetime = reminders[reminder]['datetime_text']
                rem_desc = reminders[reminder]['desc']
                print(f'ALERT: {reminder} @ {rem_datetime}')
                alert_active = True
        if alert_active == True:
            ctypes.windll.user32.MessageBoxW(None, f'Reminder alert!\nName: {exp_rem}\nDate: {rem_datetime}\nDescription: {rem_desc}', 'Elephant: Alert!', 0x40)
            del(reminders[exp_rem])
            write_json('reminders.json')
            alert_active = False


# init newsapi
newsapi = NewsApiClient(api_key='2c5802617c7a4cc2959c4b89cd9d8dae')
top_headlines = newsapi.get_everything(q='COVID')

# set window attributes
window = Tk()
window.iconbitmap('elephant.ico')
window.title('Elephant')
window.geometry('435x290')
window.resizable(0,0)

label = Label(window, text='Elephant', font=('Balsamiq Sans', 24)) # app label
label.grid(column=1, row=0)

news_btn = Button(window, text='News & Stats', command = show_news) # News button (using news api)
news_btn.grid(column=1, row=21, pady=(6, 0))

submit_btn = Button(window, text='Submit', command = submit) # Submit button
submit_btn.grid(column=1, row=20, pady=(6, 0))

view_btn = Button(window, text='View reminders', command = view_reminders)
view_btn.grid(column=1, row=22, pady=(6, 0))

reminder_label = Label(window, text='Reminder', font=('Roboto', 12))
reminder_label.grid(column=0, row=2)
reminder = Entry(window, width=36)
reminder.grid(column=1, row=2, pady=(6,0), padx=(40,10))

desc_label = Label(window, text='Description', font=('Roboto', 12))
desc_label.grid(column=0, row=3)
desc = Entry(window, width=36)
desc.grid(column=1, row=3, pady=(6,0), padx=(40,10))

date_label = Label(window, text='Date', font=('Roboto', 12))
date_label.grid(column=0, row=4)
date = Combobox(window, width=12)
date['values'] = date_list_str
date.current(0)
date.grid(column=1, row=4, pady=(6,0))

time_label = Label(window, text='Time (24-h format)', font=('Roboto', 12))
time_label.grid(column=0, row=6)
time_entry = Entry(window, width=10)
time_entry.grid(column=1, row=6, pady=(6,0))

# run the program
class RepeatTimer(threading.Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

check_thread = RepeatTimer(2.5, check_timer)
check_thread.start()

#Redefine exit to stop timer
def exitProtocol():
    window.destroy()
    check_thread.cancel()
    print('Elephant closed succesfully!')

window.protocol('WM_DELETE_WINDOW', exitProtocol)
check_start()
mainloop()