from tkinter import *
from tkinter import ttk
from pokeapi import get_pokemon_info

def main():
    #create window
    root = Tk()
    root.title('Pokedex GUI')

    #create frames
    frm_input = ttk.Frame(root)
    frm_input.grid(row=0, column=0, columnspan=2)

    frm_info = ttk.LabelFrame(root, text="Info")
    frm_info.grid(row=1, column=0)

    frm_stats = ttk.LabelFrame(root, text="Stats")
    frm_stats.grid(row=1, column=1)

    #populate user input frame
    lbl_name = ttk.Label(frm_input, text="Pokemon name: ")
    lbl_name.grid(row=0, column=0, padx=10, pady=10)

    entry_name = ttk.Entry(frm_input)
    entry_name.grid(row=0, column=1, padx=10, pady=10)

    def btn_get_info_click():
        name = entry_name.get()
        poke_dict = get_pokemon_info(name)
        if poke_dict:
            lbl_height_val['text'] = str(poke_dict['height']) + 'dm'
            lbl_weight_val['text'] = str(poke_dict['weight']) + 'hg'

    btn_getinfo = ttk.Button(frm_input, text="Get info")
    btn_getinfo.grid(row=0, column=2, padx=10, pady=10)

    #populate stats frame
    lbl_hp = ttk.Label(frm_stats, text="HP: ")
    lbl_hp.grid(row=0, column=0, padx=10, pady=10)
    prg_hp = ttk.Progressbar()
    prg_hp.grid(row=0, column=1, padx=10, pady=10)

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
