import os
from GlobalConfig import MusicConfig

# Note: 存放关于音符持续时间，音高的信息
class Note:
    def __init__(self,num,pitch,duration):
        self.num = num 
        self.pitch = pitch
        self.duration = duration
    
    def __repr__(self) -> str:
        return f"{self.num}({self.pitch}) duration:{self.duration}"

    @property
    def abs_int_note(self)->int:
        if self.num > 0 and self.num <= 7 and self.duration > 0:
            return (2 - self.pitch) * 7 + self.num
        else:
            return 0 if self.num == 0 else -1  
        # (2-pitch[i])*7+note[i]

    @staticmethod
    def convert_from_predicted_list(lst_note,lst_pitch,lst_dur):
        note_list = []
        for i in range(len(lst_note)):
            note : Note = Note(lst_note[i],lst_pitch[i],lst_dur[i])
            note_list.append(note)

        return note_list

    @staticmethod
    def music_save(music_name,note_list,base=5):
        path_name = os.path.join(MusicConfig.prefix,music_name)
        # if os.path.exists(path_name):
        #     raise Exception("File had exists")
        
        file = open(path_name,'w')
        file.write(str(base) + '\n')
        for note in note_list:
            note : Note
            dur = note.duration if note.duration < 3 else 2
            file.write(f"{note.num}#{note.pitch}#{dur}\n")
        

    @staticmethod
    def music_read(music_name):
        path_name = os.path.join(MusicConfig.prefix,music_name)
        if not os.path.exists(path_name):
            raise Exception("file not exists")
        
        file = open(path_name,'r')
        lines = file.readlines()
        lines = [line.replace('\n','') for line in lines]
        note_list = []
        base = int(lines[0])
        lines.pop(0)
        for i,line in enumerate(lines):
            info = [int(item) for item in line.split('#')]
            if info[0] in range(0,8):
                note_list.append(Note(info[0],info[1],1/(2**(info[2]-1))))
            elif info[0] == 9:
                if len(note_list) > 0:
                    note_list[len(note_list)-1].duration *= 1.5
            elif info[0] == 10:
                if len(note_list) > 0:
                    note_list[len(note_list)-1].duration += 1


        return note_list,base



class Music:
    def __init__(self,song_notes):
        self.song_notes = song_notes
        self.ptr = -1

    def is_over(self):
        return self.ptr == len(self.song_notes) - 1

    def next_note(self):
        if not self.is_over():
            self.ptr += 1

    def get_currrent_note(self)->Note:
        return self.song_notes[self.ptr]

    def play_from_start(self):
        self.ptr = 0

    def get_progress(self) -> float:
        return (1 + self.ptr ) / len(self.song_notes)
        