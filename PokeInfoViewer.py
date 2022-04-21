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
    frm_info.grid(row=1, column=0, padx=20, pady=20)
    #bottom right
    frm_stats = ttk.LabelFrame(root, text="Stats")
    frm_stats.grid(row=1, column=1, padx=20, pady=20)

    #populate user input frame
    lbl_name = ttk.Label(frm_input, text="Pokemon name: ")
    lbl_name.grid(row=0, column=0, padx=(10,0), pady=10)

    ent_name = ttk.Entry(frm_input)
    ent_name.grid(row=0, column=1, padx=(0, 10), pady=10)


    def btn_get_info_click():
        name = ent_name.get()
        poke_dict = get_pokemon_info(name)
        if poke_dict:
            #
            lbl_height_val['text'] = str(poke_dict['height']) + 'dm'
            lbl_weight_val['text'] = str(poke_dict['weight']) + 'hg'

            types_list = [t['type']['name'] for t in poke_dict['types']]
            lbl_type_val['text'] = ', '.join(types_list)

            prg_hp['value'] = poke_dict['stats'][0]['base_stat']
            prg_attack['value'] = poke_dict['stats'][1]['base_stat']
            prg_defense['value'] = poke_dict['stats'][2]['base_stat']
            prg_specialattack['value'] = poke_dict['stats'][3]['base_stat']
            prg_specialdefense['value'] = poke_dict['stats'][4]['base_stat']
            prg_speed['value'] = poke_dict['stats'][5]['base_stat']
            
    
    btn_getinfo = ttk.Button(frm_input, text="Get info", command=btn_get_info_click)
    btn_getinfo.grid(row=0, column=2, padx=10, pady=10)
    
    #populate info frame
    lbl_height = ttk.Label(frm_info, text='Height: ')
    lbl_height.grid(row=0, column=1, padx=10, pady=10)
    lbl_height_val = ttk.Label(frm_info, text="TBD")
    lbl_height_val.grid(row=0, column=2, padx=10, pady=10)

    lbl_weight = ttk.Label(frm_info, text='Weight: ')
    lbl_weight.grid(row=1, column=1, padx=10, pady=10)
    lbl_weight_val = ttk.Label(frm_info, text="TBD")
    lbl_weight_val.grid(row=1, column=2, padx=10, pady=10)

    lbl_type = ttk.Label(frm_info, text='Type: ')
    lbl_type.grid(row=2, column=1, padx=10, pady=10)
    lbl_type_val = ttk.Label(frm_info, text="TBD")
    lbl_type_val.grid(row=2, column=2, padx=10, pady=10)

    #populate stats frame
    lbl_hp = ttk.Label(frm_stats, text="HP: ")
    lbl_hp.grid(row=0, column=0, padx=10, pady=5)
    prg_hp = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_hp.grid(row=0, column=1, padx= 10, pady=5)

    lbl_attack = ttk.Label(frm_stats, text="Attack: ")
    lbl_attack.grid(row=1, column=0, padx=10, pady=5)
    prg_attack = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_attack.grid(row=1, column=1, padx= 10, pady=5)
    
    lbl_defense = ttk.Label(frm_stats, text="Defense: ")
    lbl_defense.grid(row=2, column=0, padx=10, pady=5)
    prg_defense = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_defense.grid(row=2, column=1, padx= 10, pady=5)

    lbl_specialattack = ttk.Label(frm_stats, text="Special Attack: ")
    lbl_specialattack.grid(row=3, column=0, padx=10, pady=5)
    prg_specialattack = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_specialattack.grid(row=3, column=1, padx= 10, pady=5)

    lbl_specialdefense = ttk.Label(frm_stats, text="Special Defense: ")
    lbl_specialdefense.grid(row=4, column=0, padx=10, pady=5)
    prg_specialdefense = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_specialdefense.grid(row=4, column=1, padx= 10, pady=5)
    
    lbl_speed = ttk.Label(frm_stats, text="Speed: ")
    lbl_speed.grid(row=5, column=0, padx=10, pady=5)
    prg_speed = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_speed.grid(row=5, column=1, padx= 10, pady=5)

    root.mainloop()

main()
