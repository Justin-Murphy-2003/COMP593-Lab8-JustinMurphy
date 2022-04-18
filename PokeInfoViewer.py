from tkinter import *
from tkinter import ttk
from pokeapi import get_pokemon_info

def main():
    #create window
    root = Tk()
    root.title('Pokedex GUI')

    #create frames
    #top frame
    frm_input = ttk.Frame(root)
    frm_input.grid(row=0, column=0, columnspan=2)
    #bottom left
    frm_info = ttk.LabelFrame(root, text="Info")
    frm_info.grid(row=1, column=0)
    #bottom right
    frm_stats = ttk.LabelFrame(root, text="Stats")
    frm_stats.grid(row=1, column=1)

    #populate user input frame
    lbl_name = ttk.Label(frm_input, text="Pokemon name: ")
    lbl_name.grid(row=0, column=0, padx=(10,0), pady=10)

    entry_name = ttk.Entry(frm_input)
    entry_name.grid(row=0, column=1, padx=(0, 10), pady=10)

    btn_getinfo = ttk.Button(frm_input, text="Get info")
    btn_getinfo.grid(row=0, column=2, padx=10, pady=10)

    def btn_get_info_click():
        name = entry_name.get()
        poke_dict = get_pokemon_info(name)
        if poke_dict:
            lbl_height_val['text'] = str(poke_dict['height']) + 'dm'
            lbl_weight_val['text'] = str(poke_dict['weight']) + 'hg'
    
    #populate stats frame
    lbl_hp = ttk.Label(frm_stats, text="HP: ")
    lbl_hp.grid(row=0, column=0, padx=10, pady=5)
    prg_hp = ttk.Progressbar(frm_stats)
    prg_hp.grid(row=0, column=1, padx= 10, pady=5)

    lbl_attack = ttk.Label(frm_stats, text="Attack: ")
    lbl_attack.grid(row=1, column=0, padx=10, pady=5)
    prg_attack = ttk.Progressbar(frm_stats)
    prg_attack.grid(row=1, column=1, padx= 10, pady=5)
    
    lbl_defense = ttk.Label(frm_stats, text="Defense: ")
    lbl_defense.grid(row=2, column=0, padx=10, pady=5)
    prg_defense = ttk.Progressbar(frm_stats)
    prg_defense.grid(row=2, column=1, padx= 10, pady=5)

    lbl_specialattack = ttk.Label(frm_stats, text="Special Attack: ")
    lbl_specialattack.grid(row=3, column=0, padx=10, pady=5)
    prg_specialattack = ttk.Progressbar(frm_stats)
    prg_specialattack.grid(row=3, column=1, padx= 10, pady=5)

    lbl_specialdefense = ttk.Label(frm_stats, text="Special Defense: ")
    lbl_specialdefense.grid(row=4, column=0, padx=10, pady=5)
    prg_specialdefense = ttk.Progressbar(frm_stats)
    prg_specialdefense.grid(row=4, column=1, padx= 10, pady=5)
    
    lbl_speed = ttk.Label(frm_stats, text="Speed: ")
    lbl_speed.grid(row=5, column=0, padx=10, pady=5)
    prg_speed = ttk.Progressbar(frm_stats)
    prg_speed.grid(row=5, column=1, padx= 10, pady=5)

    #populate info frame
    lbl_height = ttk.Label(frm_info, text='Height: ')
    lbl_height.grid(row=0, column=1, padx=10, pady=10)
    lbl_height_val = ttk.Label(frm_info, text="TBD")
    lbl_height_val.grid(row=0, column=2, padx=10, pady=10)

    lbl_weight = ttk.Label(frm_info, text='Weight: ')
    lbl_weight.grid(row=1, column=1, padx=10, pady=10)
    lbl_weight_val = ttk.Label(frm_info, text="TBD")
    lbl_height_val.grid(row=1, column=2, padx=10, pady=10)

    lbl_type = ttk.Label(frm_info, text='Type: ')
    lbl_type.grid(row=2, column=1, padx=10, pady=10)
    lbl_type_val = ttk.Label(frm_info, text='TBD')
    lbl_type_val.grid(row=2, column=2, padx=10, pady=10)

    root.mainloop()

main()
