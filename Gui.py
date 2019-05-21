import tkinter as tk
from PIL import ImageTk, Image, ImageOps, ImageDraw
import plotly.plotly as py
import plotly.graph_objs as go
from copy import deepcopy
from collections import OrderedDict
import numpy as np
import re
py.sign_in('', '')


class Gamemap():
    def __init__(self):
        self.startGui()
        self.startHeatmap()
        self.wards = OrderedDict()
        self.ward_backup = OrderedDict()
        self.window.mainloop()

    def startGui(self):
        self.window = tk.Tk()
        self.pop_up('Menu')
        self.menubar = tk.Menu(self.window)
        self.menubar.add_command(label="New", command=self.new)
        self.menubar.add_command(label="Load", command=self.load)
        self.window.config(menu=self.menubar)
        self.M = []
        self.Canvas = tk.Canvas(self.window, width=400, height=810)
        self.mainCanvas= tk.Canvas(self.window, width=768, height=810)
        self.img = Image.open('srift.jpg')
        self.img = self.img.resize((770, 774), Image.ANTIALIAS)
        self.mapimg = ImageTk.PhotoImage(self.img)
        self.mainCanvas.create_image(385, 387, image=self.mapimg)
        self.mainCanvas.bind("<Control-Button-1>", self.sightstone)
        self.mainCanvas.bind("<Alt-Button-1>", self.control_ward)
        self.mainCanvas.bind("<Control-Button-3>", self.trinket_ward)
        self.mainCanvas.bind("<Alt-Button-3>", self.farsight)
        self.mainCanvas.pack(side="left", fill="x", expand="yes")
        self.sightstoneimg = Image.open('Sightstone_item.png')
        self.sightstoneimg = self.sightstoneimg.resize((50,50), Image.ANTIALIAS)
        self.sightstoneimg = ImageTk.PhotoImage(self.sightstoneimg)
        self.controlwardimg = Image.open('Control_Ward.png')
        self.controlwardimg = self.controlwardimg.resize((50, 50), Image.ANTIALIAS)
        self.controlwardimg = ImageTk.PhotoImage(self.controlwardimg)
        self.totemwardimg = Image.open('Warding_Totem_item.png')
        self.totemwardimg = self.totemwardimg.resize((50, 50), Image.ANTIALIAS)
        self.totemwardimg = ImageTk.PhotoImage(self.totemwardimg)
        self.farsightwardimg = Image.open('Farsight_Alteration_item.png')
        self.farsightwardimg = self.farsightwardimg.resize((50, 50), Image.ANTIALIAS)
        self.farsightwardimg = ImageTk.PhotoImage(self.farsightwardimg)
        self.Canvas.create_text(155, 45, text='Ctrl + Left Click')
        self.Canvas.create_text(220, 90, text='Alt + Left Click')
        self.Canvas.create_text(155, 135, text='Ctrl + Right Click')
        self.Canvas.create_text(220, 180, text='Alt + Right Click')
        self.canvas_sstone_button = tk.Button(self.window, image=self.sightstoneimg, width=50, height=50,
                                              compound='left', command=self.sstone_callback, bg='black', padx=1, pady=1)
        self.canvas_cward_button = tk.Button(self.window, image=self.controlwardimg, width=50, height=50,
                                             compound='left', command=self.cward_callback, bg='red', padx=1, pady=1)
        self.canvas_tward_button = tk.Button(self.window, image=self.totemwardimg, width=50, height=50,
                                             compound='left', command=self.tward_callback,bg='yellow', padx=1, pady=1)
        self.canvas_farsight_button = tk.Button(self.window, image=self.farsightwardimg, width=50, height=50,
                                                compound='left', command=self.fward_callback, bg='blue', padx=1, pady=1)
        self.Canvas.create_window(75, 75, anchor='s', window=self.canvas_sstone_button)
        self.Canvas.create_window(300, 120, anchor='s', window=self.canvas_cward_button)
        self.Canvas.create_window(75, 165, anchor='s', window=self.canvas_tward_button)
        self.Canvas.create_window(300, 210, anchor='s', window=self.canvas_farsight_button)
        canvas_mtx_button = tk.Button(self.window, text='Set Data', width=10, anchor='s', command=self.setData)
        canvas_htmp_button = tk.Button(self.window, text='Heatmap', width=10, anchor='s', command=self.Heatmap_callback)
        canvas_small_data_button = tk.Button(self.window, text='Small Data', width=10, anchor='s',
                                             command=self.small_data)
        canvas_big_data_button = tk.Button(self.window, text='Big Data', width=10, anchor='s',
                                             command=self.big_data)
        self.undoimg = Image.open('undo.png')
        self.undoimg = self.undoimg.resize((30, 30), Image.ANTIALIAS)
        self.undoimg = ImageTk.PhotoImage(self.undoimg)
        canvas_undo_button = tk.Button(self.window, image=self.undoimg, width=30, height=30,
                                                compound='left', command=self.undo, padx=1, pady=1)
        self.Canvas.create_window(150, 305, anchor='s', window=canvas_mtx_button)
        self.Canvas.create_window(250, 305, anchor='s', window=canvas_htmp_button)
        self.Canvas.create_window(150, 265, anchor='s', window=canvas_small_data_button)
        self.Canvas.create_window(250, 265, anchor='s', window=canvas_big_data_button)
        self.Canvas.create_window(200, 345, anchor='s', window=canvas_undo_button)
        self.scroll_bar()
        self.Canvas.pack()
        self.strings = ['sward', 'cward', 'tward', 'fward']
        self.sward_color, self.cward_color, self.tward_color, self.fward_color = 'black', 'red', 'yellow', 'blue'
        self.dump = OrderedDict()
        self.selected_match = ''

    def scroll_bar(self):
        self.var1 = tk.IntVar()
        self.check_button = tk.Checkbutton(self.Canvas, text='Time Heatmap', variable=self.var1,
                                           command=self.activate_scroll_bar)
        self.scale_bar = tk.Scale(self.Canvas, from_=0, to=30, length=200, tickinterval=5, orient='horizontal',
                                  state='disabled')
        self.check_button.place(x=25, y=600)
        self.scale_bar.place(x=30, y=650)

    def activate_scroll_bar(self):
        if self.var1 == 1:
            self.scale_bar.configure(state='normal')
            self.var1 = 0
        else:
            self.scale_bar.configure(state='disabled')
            self.var1 = 1

    def sstone_callback(self):
        relief = self.canvas_sstone_button.cget('relief')
        if relief != 'raised':
            self.canvas_sstone_button.config(borderwidth=1, relief='raised')
            self.wards = self.ward_backup
        else:
            self.canvas_sstone_button.config(borderwidth=3, relief='solid')

    def cward_callback(self):
        relief = self.canvas_cward_button.cget('relief')
        if relief != 'raised':
            self.canvas_cward_button.config(borderwidth=1, relief='raised')
            self.wards = self.ward_backup
        else:
            self.canvas_cward_button.config(borderwidth=3, relief='solid')

    def tward_callback(self):
        relief = self.canvas_tward_button.cget('relief')
        if relief != 'raised':
            self.canvas_tward_button.config(borderwidth=1, relief='raised')
            self.wards = self.ward_backup
        else:
            self.canvas_tward_button.config(borderwidth=3, relief='solid')

    def fward_callback(self):
        relief = self.canvas_farsight_button.cget('relief')
        if relief != 'raised':
            self.canvas_farsight_button.config(borderwidth=1, relief='raised')
            self.wards = self.ward_backup
        else:
            self.canvas_farsight_button.config(borderwidth=3, relief='solid')

    def selec_button_pressed(self, relief):
        for (rel, string) in relief:
            if rel == 'solid':
                return True
        return False

    def selection(self):
        relief_1 = self.canvas_sstone_button.cget('relief')
        relief_2 = self.canvas_cward_button.cget('relief')
        relief_3 = self.canvas_tward_button.cget('relief')
        relief_4 = self.canvas_farsight_button.cget('relief')
        relief = [(relief_1, 'sward'), (relief_2, 'cward'), (relief_3, 'tward'), (relief_4, 'fward')]
        if self.selec_button_pressed(relief):
            solid_buttons = [string for (relief_d, string) in relief if relief_d == 'solid']
            wards = []
            self.ward_backup = deepcopy(self.wards)
            for key in self.ward_backup.keys():
                for string in solid_buttons:
                    if string in key:
                        wards.append((key, self.ward_backup[key]))
            ward_dic = {key: value for (key, value) in wards}
            return ward_dic
        else:
            return self.wards

    def sightstone(self, event):
        n, self.string, obj = len(self.wards) + 1, 'sward ', self.find_obj(event)
        self.string_color = self.sward_color
        if not obj:
            output = self.circle(17, self.string)
            sward_img = ImageTk.PhotoImage(output)
            sward_id = self.mainCanvas.create_image(event.x, event.y, image=sward_img,
                                                    tags=('ward', self.string + '%d' % n))
            self.dump.update(
                {self.string + '%d' % n: {'obj': {self.string: {'misc':(sward_img, sward_id), 'stack': 1}},
                                          'stack_count': 0}})
        else:
            tag = self.find_tag(obj)
            if self.dump[tag]['stack_count'] == 0:
                if self.string in self.dump[tag]['obj']:
                    self.dump[tag]['obj'][self.string]['stack'] += 1
                    self.stack(event, obj, self.dump[tag]['obj'][self.string]['stack'], tag)
                else:
                    self.dump[tag]['obj'].update({self.string: {'misc': ('blank', 'blank'), 'stack': 1}})
                    self.stack(event, obj, 1, tag)
            else:
                if self.string in self.dump[tag]['obj']:
                    self.dump[tag]['obj'][self.string]['stack'] += 1
                    if self.dump[tag]['obj'][self.string]['stack'] == 2:
                        self.multi_stack(event, obj, self.dump[tag]['obj'][self.string]['stack'], tag)
                    else:
                        self.multi_stack(event, obj, self.dump[tag]['obj'][self.string]['stack'], tag, False)
                else:
                    self.dump[tag]['obj'].update({self.string: {'misc': ('blank', 'blank'), 'stack': 1}})
                    self.multi_stack(event, obj, 1, tag)
        self.pop_up('Ward', 'Timestamp')
        self.wards.update({self.string+'%d' % n: [(event.x, event.y)]})
        #print('You clicked at:', event.x,' ', event.y)

    def control_ward(self, event):
        n, self.string, obj = len(self.wards)+1, 'cward ', self.find_obj(event)
        self.string_color = self.cward_color
        if not obj:
            output = self.circle(17, self.string)
            cward_img = ImageTk.PhotoImage(output)
            cward_id = self.mainCanvas.create_image(event.x, event.y, image=cward_img,
                                                    tags=('ward', self.string + '%d' % n))
            self.dump.update(
                {self.string + '%d' % n: {'obj': {self.string: {'misc': (cward_img, cward_id), 'stack': 1}},
                                          'stack_count': 0}})
        else:
            tag = self.find_tag(obj)
            if self.dump[tag]['stack_count'] == 0:
                if self.string in self.dump[tag]['obj']:
                    self.dump[tag]['obj'][self.string]['stack'] += 1
                    self.stack(event, obj, self.dump[tag]['obj'][self.string]['stack'], tag)
                else:
                    self.dump[tag]['obj'].update({self.string: {'misc': ('blank', 'blank'), 'stack': 1}})
                    self.stack(event, obj, 1, tag)
            else:
                if self.string in self.dump[tag]['obj']:
                    self.dump[tag]['obj'][self.string]['stack'] += 1
                    if self.dump[tag]['obj'][self.string]['stack'] == 2:
                        self.multi_stack(event, obj, self.dump[tag]['obj'][self.string]['stack'], tag)
                    else:
                        self.multi_stack(event, obj, self.dump[tag]['obj'][self.string]['stack'], tag, False)
                else:
                    self.dump[tag]['obj'].update({self.string: {'misc': ('blank', 'blank'), 'stack': 1}})
                    self.multi_stack(event, obj, 1, tag)
        self.pop_up('Ward', 'Timestamp')
        self.wards.update({self.string+'%d' % n: [(event.x, event.y)]})

    def trinket_ward(self, event):
        n, self.string, obj = len(self.wards) + 1, 'tward ', self.find_obj(event)
        self.string_color = self.tward_color
        if not obj:
            output = self.circle(17, self.string)
            tward_img = ImageTk.PhotoImage(output)
            tward_id = self.mainCanvas.create_image(event.x, event.y, image=tward_img,
                                                    tags=('ward', self.string + '%d' % n))
            self.dump.update(
                {self.string + '%d' % n: {'obj': {self.string: {'misc': (tward_img, tward_id), 'stack': 1}},
                                          'stack_count': 0}})
        else:
            tag = self.find_tag(obj)
            if self.dump[tag]['stack_count'] == 0:
                if self.string in self.dump[tag]['obj']:
                    self.dump[tag]['obj'][self.string]['stack'] += 1
                    self.stack(event, obj, self.dump[tag]['obj'][self.string]['stack'], tag)
                else:
                    self.dump[tag]['obj'].update({self.string: {'misc': ('blank', 'blank'), 'stack': 1}})
                    self.stack(event, obj, 1, tag)
            else:
                if self.string in self.dump[tag]['obj']:
                    self.dump[tag]['obj'][self.string]['stack'] += 1
                    if self.dump[tag]['obj'][self.string]['stack'] == 2:
                        self.multi_stack(event, obj, self.dump[tag]['obj'][self.string]['stack'], tag)
                    else:
                        self.multi_stack(event, obj, self.dump[tag]['obj'][self.string]['stack'], tag, False)
                else:
                    self.dump[tag]['obj'].update({self.string: {'misc': ('blank', 'blank'), 'stack': 1}})
                    self.multi_stack(event, obj, 1, tag)
        self.pop_up('Ward', 'Timestamp')
        self.wards.update({self.string+'%d' % n: [(event.x, event.y)]})

    def farsight(self, event):
        n, self.string, obj = len(self.wards) + 1, 'fward ', self.find_obj(event)
        self.string_color = self.fward_color
        if not obj:
            output = self.circle(17, self.string)
            fward_img = ImageTk.PhotoImage(output)
            fward_id = self.mainCanvas.create_image(event.x, event.y, image=fward_img,
                                                    tags=('ward', self.string + '%d' % n))
            self.dump.update(
                {self.string + '%d' % n: {'obj': {self.string: {'misc': (fward_img, fward_id), 'stack': 1}},
                                          'stack_count': 0}})
        else:
            tag = self.find_tag(obj)
            if self.dump[tag]['stack_count'] == 0:
                if self.string in self.dump[tag]['obj']:
                    self.dump[tag]['obj'][self.string]['stack'] += 1
                    self.stack(event, obj, self.dump[tag]['obj'][self.string]['stack'], tag)
                else:
                    self.dump[tag]['obj'].update({self.string: {'misc': ('blank', 'blank'), 'stack': 1}})
                    self.stack(event, obj, 1, tag)
            else:
                if self.string in self.dump[tag]['obj']:
                    self.dump[tag]['obj'][self.string]['stack'] += 1
                    if self.dump[tag]['obj'][self.string]['stack'] == 2:
                        self.multi_stack(event, obj, self.dump[tag]['obj'][self.string]['stack'], tag)
                    else:
                        self.multi_stack(event, obj, self.dump[tag]['obj'][self.string]['stack'], tag, False)
                else:
                    self.dump[tag]['obj'].update({self.string: {'misc': ('blank', 'blank'), 'stack': 1}})
                    self.multi_stack(event, obj, 1, tag)
        self.pop_up('Ward', 'Timestamp')
        self.wards.update({self.string + '%d' % n: [(event.x, event.y)]})

    def makeentry(self, parent, caption, width=None, **options):
        l = tk.Label(parent, text=caption)
        l.pack(side=tk.LEFT)
        entry = tk.Entry(parent, **options)
        if width:
            entry.config(width=width)
        entry.bind('<Return>', self.callback)
        entry.pack(side=tk.LEFT)
        entry.focus()
        return entry

    def callback(self, event):
        n = len(self.wards)
        self.wards[self.string+'%d' % n].append(str(self.timestamp.get()))
        self.win.destroy()

    def setData(self):
        self.wards = self.selection()
        self.M_x = []
        self.M_y = []
        for i in self.wards.items():
            x = (i[1][0][0])
            y = 770 - (i[1][0][1])
            self.M_x.append(x)
            self.M_y.append(y)
        self.data['matches'][self.match_name]['y'] = self.M_y
        self.data['matches'][self.match_name]['x'] = self.M_x

    def circle(self, n, string):
        mask = Image.new('L', (n, n), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + mask.size, fill=255)
        if string == 'sward ':
            im = Image.open('Sightstone_item.png')
        elif string == 'cward ':
            im = Image.open('Control_Ward.png')
        elif string == 'tward ':
            im = Image.open('Warding_Totem_item.png')
        elif string == 'fward ':
            im = Image.open('Farsight_Alteration_item.png')
        output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
        output.putalpha(mask)
        return output

    def find_obj(self, event):
        canvas = event.widget
        x = canvas.canvasx(event.x)
        y = canvas.canvasy(event.y)
        for obj in canvas.find_closest(x, y):
            if obj != 1:
                #print(canvas.itemcget(obj, 'tags'))
                return obj
            else:
                for ob in canvas.find_closest(x, y, halo=8.5):
                    if ob != 1:
                        #print(canvas.itemcget(ob, 'tags'))
                        return ob
        return False

    def stack(self, event, obj, n, tag):
        if len(self.wards) != 1:
            m = len(self.wards) - 1
        else:
            m = len(self.wards)
        canvas, font = event.widget, ('Arial', 10, 'bold')
        coord_list = canvas.coords(obj)
        x, y = coord_list[0], coord_list[1]
        obj_tuple = canvas.find_closest(float(x), y - 17.0)
        for object in obj_tuple:
            obj_id = object
        tags = canvas.itemcget(obj, 'tags')
        spec_tags = canvas.itemcget(obj_id, 'tags')
        if 'ward' in tags and 'stack' not in tags and 'rect' not in tags:
            if obj_id == 1 or 'ward' in spec_tags and 'stack' not in spec_tags:
                text = self.mainCanvas.create_text(x, y-17, text=str(n), fill=self.string_color,
                                                   tags=('ward_stack', self.string + '%d' % m), font=font)
                rect = self.mainCanvas.create_rectangle(self.mainCanvas.bbox(text), fill='#fff',
                                                        tags=('rect', self.string + '%d' % m), outline='#fff')
                self.mainCanvas.lower(rect, text)
                ward_img = self.dump[tag]['obj'][self.string]['misc'][0]
                ward_id = self.dump[tag]['obj'][self.string]['misc'][1]
                self.dump[tag]['obj'][self.string].update({'misc': (ward_img, ward_id, text, rect)})
                self.dump[tag]['stack_count'] += 1
            elif 'ward_stack' in spec_tags or 'rect' in spec_tags:
                canvas.itemconfigure(obj_id, text=str(n))
        elif 'ward_stack' in tags:
            canvas.itemconfigure(obj, text=str(n))
        elif 'rect' in tags:
            (x0, y0, x1, y1) = canvas.bbox(obj)
            for object_id in canvas.find_enclosed(x0, y0, x1, y1):
                if 'ward_stack' in canvas.itemcget(object_id, 'tags'):
                    canvas.itemconfigure(object_id, text=str(n))

    def small_data(self):
        self.hist_norm = ''

    def big_data(self):
        self.hist_norm = 'probability density'

    def find_tag(self, obj):
        tags = self.mainCanvas.itemcget(obj, 'tags')
        st = ''
        if tags is not None:
            for string in self.strings:
                a = re.search(string, tags)
                if a is not None:
                    st = string
                    b = a.end()
                    break
            i, number = 0, ''
            for numb in tags[b::]:
                while tags[b + i] != '}':
                    number += tags[b + i]
                    i += 1
            return st + ' %d' % int(number)

    def multi_stack(self, event, obj, n, tag, change=True):
        if len(self.wards) != 1:
            m = len(self.wards) - 1
        else:
            m = len(self.wards)
        st = ''
        for string in self.strings:
            if string in tag:
               st = string
        canvas, font, n1 = event.widget, ('Arial', 10, 'bold'), len(self.wards)
        coord_list = canvas.coords(obj)
        x, y = coord_list[0], coord_list[1]
        obj_tuple = canvas.find_closest(float(x), y - 17.0)
        for object in obj_tuple:
            obj_id = object
        tags, spec_tags = canvas.itemcget(obj, 'tags'), canvas.itemcget(obj_id, 'tags')
        tag1, strings = self.find_tag(obj), []
        for i in self.dump[tag1]['obj'].keys():
            i = i[:len(i) - 1]
            strings.append(i)
            strings = self.spec_ord(strings)
        if 'ward' in tags:
            if 'stack' in tags:
                pass
            elif 'rect' in tags:
                pass
            if change:
                self.dump[tag]['stack_count'] += 1
                for objex in self.dump[tag1]['obj']:
                    if len(self.dump[tag1]['obj'][objex]['misc']) > 2:
                        text, rect = self.dump[tag1]['obj'][objex]['misc'][2], self.dump[tag1]['obj'][objex]['misc'][3]
                        self.mainCanvas.delete(rect)
                        self.mainCanvas.delete(text)
                for i in range(len(strings)):
                    text = self.mainCanvas.create_text(x + self.stack_func(i + 1), y - 17,
                                                       text=self.dump[tag1]['obj'][strings[i] + ' ']['stack'],
                                                       fill=self.color(strings[i]),
                                                       tags=('ward_stack', strings[i] + ' %d' % m), font=font)
                    rect = self.mainCanvas.create_rectangle(self.mainCanvas.bbox(text), fill='#fff',
                                                            tags=('rect', strings[i] + ' %d' % m), outline='#fff')
                    self.dump[tag1]['obj'][strings[i] + ' '].update({'misc': (self.dump[tag1]['obj'][strings[i] + ' ']['misc'][0],
                                                                   self.dump[tag1]['obj'][strings[i] + ' ']['misc'][1],
                                                                   text, rect)})
                    self.mainCanvas.lower(rect, text)

            else:
                canvas.itemconfigure(self.dump[tag1]['obj'][self.string]['misc'][2], text=str(n))
        elif 'rect' in tags:
            (x0, y0, x1, y1) = canvas.bbox(obj)
            for object_id in canvas.find_enclosed(x0, y0, x1, y1):
                if 'ward_stack' in canvas.itemcget(object_id, 'tags'):
                    canvas.itemconfigure(object_id, text=str(n))

    def stack_func(self, x):
        if x % 2 != 0:
            y = -5 * np.ceil(x / 2)**1.5
        else:
            y = 5 * (np.floor(x / 2))**1.5
        return y

    def spec_ord(self, list):
        old , new = deepcopy(list), ['', '', '', '']
        while len(old) > 0:
            stri = old.pop()
            if stri == 'sward':
                new[2] = stri
            elif stri == 'cward':
                new[0] = stri
            elif stri == 'tward':
                new[1] = stri
            elif stri == 'fward':
                new[3] = stri
        new = [i for i in new if i != '']
        return new

    def color(self, string):
        if string == 'sward':
            return self.sward_color
        elif string == 'cward':
            return self.cward_color
        elif string == 'tward':
            return self.tward_color
        elif string == 'fward':
            return self.fward_color

    def new(self):
        self.new_popup()

    def load(self, event):
        pass

    def new_popup(self):
        self.wind = tk.Toplevel()
        self.wind.wm_title('New')
        self.wind.grab_set()
        self.new_match = self.makeentry(self.wind, 'Name:')
        button = tk.Button(self.wind, text='Ok', width=10, command=self.new_callback)
        button.pack()

    def new_callback(self):
        if self.match_name == 'someone':
            self.new_match = self.new_match.get()
            self.data['matches'][self.new_match] = self.data['matches'].pop('someone')
            self.match_name = self.new_match
        else:
            self.new_match = self.new_match.get()
            self.data['matches'][self.new_match] = {"y": [], "x": []}
            self.match_name = self.new_match
        self.wind.grab_release()
        self.wind.destroy()
        self.win.destroy()
        self.mainCanvas.delete('ward')
        self.mainCanvas.delete('ward_stack')
        self.mainCanvas.delete('rect')
        self.wards, self.dump = OrderedDict(), OrderedDict()

    def undo(self):
        last_item = self.wards.popitem(last=True)
        if last_item[0] in self.dump:
            del self.dump[last_item[0]]
        else:
            pass

    def startHeatmap(self):
        self.data = {"matches": {"someone": {"y": [], "x": []}}, "mode": "classic"}
        self.hist_norm, self.match_name = '', "someone"
        self.mode_to_map = {"classic": 11}
        self.maps_info = {
            "11": {'bbox': {'x0': 0, 'y0': 0, 'x1': 770, 'y1': 774}, 'image_size': {'x': 1074, 'y': 1080}}}

    def create_map_graph(self, name, map_id):
        map_info = self.maps_info[map_id]
        map_url = "http://i.imgur.com/AidgPjd.jpg"
        top_margin = 0
        trace_dots = {'x': self.data['matches'][name]['x'], 'y': self.data['matches'][name]['y'],
                      'mode': 'markers', 'name': 'points',
                      'marker': {'color': 'black', 'opacity': 0.5, 'size': 2}, 'type': 'scatter'}
        trace_density = {'x': self.data['matches'][name]['x'], 'y': self.data['matches'][name]['y'],
                         'name': 'density', 'ncontours': 20, 'nbinsx': 70, 'nbinsy': 70,
                         'colorscale': [[0, 'rgba(255,255,255,0)'], [0.2, 'rgb(255,255,0)'], [0.5, 'rgb(255,128,0)'],
                                        [1, 'rgb(255,0,0)']], 'opacity': 0.5, 'showscale': False,
                         'type': 'histogram2dcontour',
                         'histnorm': self.hist_norm, 'contours': {'coloring': 'heatmap'}, 'line': {'width': 0}}
        layout = {'title': name, 'width': map_info['image_size']['x'], 'height': map_info['image_size']['y'] + top_margin,
                  'margin': {'b': 0, 'l': 0, 'r': 0, 't': top_margin}, 'autosize': False, 'showlegend': False,
                  'images': [{'source': map_url, 'x': 0, 'y': 1, 'sizex': 1, 'sizey': 1, 'sizing': "stretch",
                              'opacity': 0.8, 'layer': "below"}],
                  'xaxis': {'range': [map_info['bbox']['x0'], map_info['bbox']['x1']], 'showticklabels': False,
                            'showgrid': False, 'zeroline': False, 'ticks': ""},
                  'yaxis': {'range': [map_info['bbox']['y0'], map_info['bbox']['y1']], 'showticklabels': False,
                            'showgrid': False, 'zeroline': False, 'ticks': ""}}
        fig = go.Figure(data=[trace_dots, trace_density], layout=layout)
        py.plot(fig)

    def Heatmap(self):
        map_id = self.mode_to_map[self.data['mode']]
        if len(self.data['matches']) == 1:
            self.create_map_graph(self.match_name, str(map_id))
        else:
            self.create_map_graph(self.selected_match, str(map_id))

    def Heatmap_callback(self):
        if len(self.data['matches']) == 1:
            self.Heatmap()
        else:
            av_x_list, av_y_list = [], []
            for match in self.data['matches']:
                if 'Average' not in match:
                    av_x_list.extend(self.data['matches'][match]['x'])
                    av_y_list.extend(self.data['matches'][match]['y'])
            self.match_name = self.match_name[0:len(self.match_name) - 2] + ' Average'
            self.data['matches'][self.match_name] = {"y": av_y_list, "x": av_x_list}
            self.pop_up('Heatmap')

    def pop_up(self, string1, string2=''):
        self.win = tk.Toplevel()
        self.win.wm_title(string1)
        if string1 == 'Ward':
            self.timestamp = self.makeentry(self.win, string2+':')
            button = tk.Button(self.win, text='Ok', width=10, command=self.callback)
            button.pack()
        elif string1 == 'Menu':
            self.win.grab_set()
            self.win.geometry('{}x{}'.format(200, 100))
            button1 = tk.Button(self.win, text='New', width=10, command=self.new)
            button2 = tk.Button(self.win, text='Load', width=10, command=self.load)
            button1.pack()
            button2.pack()
            self.win.focus()
        elif string1 == 'Heatmap':
            mainframe = tk.Frame(self.win)
            mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
            mainframe.columnconfigure(0, weight=1)
            mainframe.rowconfigure(0, weight=1)
            mainframe.pack(pady=50, padx=50)
            self.tkvar = tk.StringVar(self.win)
            choices = {match for match in self.data['matches']}
            self.tkvar.set(self.match_name)
            popupMenu = tk.OptionMenu(mainframe, self.tkvar, *choices)
            tk.Label(mainframe, text="Choose a match").grid(row=1, column=1)
            popupMenu.grid(row=2, column=1)
            self.tkvar.trace('w', self.change_dropdown)
            button = tk.Button(mainframe, text='Generate', width=10, command=self.Heatmap)
            button.grid(column=1, sticky=tk.S)
            #if 'Average' in self.selected_match:
            #    self.pop_up('choose_matches')
        elif string1 == 'choose_matches':
            pass

    def change_dropdown(self, *args):
        self.selected_match = self.tkvar.get()

H = Gamemap()