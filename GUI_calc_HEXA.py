import HEXA_calc_twindow
import math

class HEXA_calc:
    def __init__(self):
        self.select_job = ""
        self.damage_add = 0
        self.attack_num_add = 0
    def input_mastery(self, skill_level):
        self.skill_level = skill_level       
        self.damage = self.skill_damage + self.skill_level * self.skill_add
        self.damage = round(self.damage)
        self.attack_num = self.attack_num * self.skill_add_attack

        #Pathfinder
        if(self.name == "Cursed Arrows"):
            self.attack_num = round(self.attack_num - ((30-self.skill_level)*0.34))

        self.text = "ダメージ:" + str(self.damage) + "%  攻撃回数:" + str(self.attack_num)

        if(self.ct > 0):
            self.text = (self.text + "  CT:" + str(self.ct) + "秒")
        if(self.f_at > 0):
            self.text = ("ダメージ:" + str(self.damage) + "%  攻撃回数:" + str(self.attack_num) + "  [FainalAttack]追加攻撃確率:" +str(self.f_at) + "%")
        if(self.passive):
             self.text = ("PASSIVE :" + str(self.damage))


    def input_add(self):

        self.skill2_damage_origin = 0
        self.damage_add = self.skill_damage_add + self.skill_level * self.skill_add_add
        self.attack_num_add = self.skill_o_t_add * self.skill_o_t_add_attack
        
        if(self.add_passive):
            self.text = self.text + ("  addPASSIVE :" + str(self.damage_add))
        else:
            self.text = (self.text
                                + "  AddAtack:" + str(self.damage_add) + "%  攻撃回数:" + str(self.attack_num_add))
        
            
        skill_2_data = False
        if(self.dic.get(self.select_job, {}).get("origin_skill", {}).get("skill_2")):
            skill_2_data = True
        if skill_2_data:
            self.skill2_damage_origin = self.skill2_damage + self.skill_level * self.skill2_add
            self.skill2_attack_num_origin = self.skill2_attack_num * self.skill2_add_attack
            self.text = (self.text
                                    + "  追加のスキル:" + str(self.skill2_damage) + "%  攻撃回数:" + str(self.skill2_attack_num_origin))
            skill_2_data = False
        else:
            pass


    def input_set(self, hexa_dic, mastery, skill, dic_add):
        self.dic = hexa_dic

        self.name            = hexa_dic[self.select_job][mastery][skill]["name"] 
        self.skill_damage    = hexa_dic[self.select_job][mastery][skill]["damage"] 
        self.attack_num      = hexa_dic[self.select_job][mastery][skill]["number_o_t"] 
        self.skill_add       = hexa_dic[self.select_job][mastery][skill]["add"]
        self.skill_add_attack= hexa_dic[self.select_job][mastery][skill]["add_attack"]
        self.add_effect      = hexa_dic[self.select_job][mastery][skill]["add_effect"]
        self.f_at            = hexa_dic[self.select_job][mastery][skill]["f_Probability"]
        self.passive         = hexa_dic[self.select_job][mastery][skill]["passive"]
        self.ct              = hexa_dic[self.select_job][mastery][skill]["ct"]
        self.dam             = hexa_dic[self.select_job][mastery][skill]["dam"] 
        self.boss_dam        = hexa_dic[self.select_job][mastery][skill]["boss_dam"]
        self.fainal_dam      = hexa_dic[self.select_job][mastery][skill]["fainal_dam"]
        self.def_a           = hexa_dic[self.select_job][mastery][skill]["def_a"]

        if(self.add_effect):
            self.skill_damage_add    = dic_add[self.select_job][mastery][self.name]["damage"]
            self.skill_add_add       = dic_add[self.select_job][mastery][self.name]["add"]
            self.skill_o_t_add       = dic_add[self.select_job][mastery][self.name]["number_o_t"]
            self.skill_o_t_add_attack= dic_add[self.select_job][mastery][self.name]["add_attack"]
            self.add_passive         = dic_add[self.select_job][mastery][self.name]["passive"]

        #print(self.name)
 

class origin_calc(HEXA_calc):
    
        def input_origin(self, skill_level):
            self.skill_level = skill_level       
            self.damage_origin = self.skill_damage + self.skill_level * self.skill_add
            self.attack_num = self.attack_num * self.skill_add_attack
            self.text = "ダメージ:" + str(self.damage_origin) + "%  攻撃回数:" + str(self.attack_num)

            self.input_add()
    
        def input_set_origin(self, dic):
            self.dic = dic
            self.name            = dic[self.select_job]["origin_skill"]["skill_1"]["name"] 
            self.skill_damage    = dic[self.select_job]["origin_skill"]["skill_1"]["damage"] 
            self.attack_num      = dic[self.select_job]["origin_skill"]["skill_1"]["number_o_t"] 
            self.skill_add       = dic[self.select_job]["origin_skill"]["skill_1"]["add"]
            self.skill_add_attack= dic[self.select_job]["origin_skill"]["skill_1"]["add_attack"]
            self.boss_dam        = dic[self.select_job]["origin_skill"]["skill_1"]["boss_dam"]
            self.def_a           = dic[self.select_job]["origin_skill"]["skill_1"]["def_a"]

            self.skill_damage_add    = dic[self.select_job]["origin_skill"]["adi_at"]["damage"]
            self.skill_add_add       = dic[self.select_job]["origin_skill"]["adi_at"]["add"]
            self.skill_o_t_add       = dic[self.select_job]["origin_skill"]["adi_at"]["number_o_t"]
            self.skill_o_t_add_attack= dic[self.select_job]["origin_skill"]["adi_at"]["add_attack"]
            
            self.add_passive = False
            
            skill_2_data = False
            if(dic.get(self.select_job, {}).get("origin_skill", {}).get("skill_2")):
                skill_2_data = True
            if skill_2_data:
                self.skill2_damage    = dic[self.select_job]["origin_skill"]["skill_2"]["damage"] 
                self.skill2_attack_num= dic[self.select_job]["origin_skill"]["skill_2"]["number_o_t"] 
                self.skill2_add       = dic[self.select_job]["origin_skill"]["skill_2"]["add"]
                self.skill2_add_attack= dic[self.select_job]["origin_skill"]["skill_2"]["add_attack"]
                self.skill2_boss_dam  = dic[self.select_job]["origin_skill"]["skill_2"]["boss_dam"]
                self.skill2_def_a     = dic[self.select_job]["origin_skill"]["skill_2"]["def_a"]
                skill_2_data = False
            else:
                pass


class ascent_calc(HEXA_calc):
    
        def input_ascent(self, damage,
                            skill_level):
            self.skill_level = skill_level       
            damage = self.skill_damage + self.skill_level * self.skill_add
            attack_num = self.attack_num * self.skill_add_attack
            self.text = "ダメージ:" + str(damage) + "%  攻撃回数:" + str(attack_num)

            if(self.skill_damage_add > 0):
                self.input_add()

    
        def input_set_ascent(self, dic):
            self.name            = dic[self.select_job]["ascent_skill"]["skill_1"]["name"] 
            self.skill_damage    = dic[self.select_job]["ascent_skill"]["skill_1"]["damage"] 
            self.attack_num      = dic[self.select_job]["ascent_skill"]["skill_1"]["number_o_t"] 
            self.skill_add       = dic[self.select_job]["ascent_skill"]["skill_1"]["add"]
            self.skill_add_attack= dic[self.select_job]["ascent_skill"]["skill_1"]["add_attack"]
            self.boss_dam        = dic[self.select_job]["ascent_skill"]["skill_1"]["boss_dam"]
            self.def_a           = dic[self.select_job]["ascent_skill"]["skill_1"]["def_a"]

            self.skill_damage_add    = dic[self.select_job]["ascent_skill"]["adi_at"]["damage"]
            self.skill_add_add       = dic[self.select_job]["ascent_skill"]["adi_at"]["add"]
            self.skill_o_t_add       = dic[self.select_job]["ascent_skill"]["adi_at"]["number_o_t"]
            self.skill_o_t_add_attack= dic[self.select_job]["ascent_skill"]["adi_at"]["add_attack"]
