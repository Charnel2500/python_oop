class Fighter(object):

    total = 0
    def __init__(self, name, attack, hp, defense, regeneration, description):
        self.name = name
        self.attack = attack
        self.hp = hp
        self.defense = defense
        self.regeneration = regeneration
        self.description = description
        Fighter.total += 1

    def talk(self):
        print("Good choose. My name is " + self.name + ".\n")
        print("This is my description: \n" + self.description + ".\n")


class Outworld_Fighter(Fighter):
    def __str__(self):
        rep = "I am outworld fighter. \n"
        return rep

class Netherrealm_Fighter(Fighter):
    def __str__(self):
        rep = "I am netherrealm fighter. \n"
        return rep

class Marial_Artist_Fighter(Fighter):
    def __str__(self):
        rep = "I am martial artist. \n"
        return rep

class Spec_Ops_Fighter(Fighter):
    def __str__(self):
        rep = "I am Spec Ops. \n"
        return rep

kitana = Outworld_Fighter("Kitana",100, 1200, 80, 50, "Kitana is the daughter of the one time rulers of Edenia King Jerod and Queen Sindel. She was no more than just a few years old when Jerod's best warriors lost 10 Mortal Kombat tournaments to Outworld's warriors. As Outworld's Emperor Shao Kahn invades Edenia, he kills Jerod and takes Sindel as his wife. Soon thereafter, Sindel committs suicide, leaving Kitana at the whim of the power hungry Emperor. Kahn takes the infant child of Jerod and Sindel and raises her as her personal assassin. Then, Shang Tsung creates a crotesque Tarkatan clone of Kitana named Mileena in which to be raised along with Kitana who would recognized her (for a time) as her twin sister. Though she would not compete in the Earthrealm tournaments but would do what she can do make her Emperor proud in his own tournament in Outworld")

shao_kahn = Outworld_Fighter("Shao Kahn",120, 1000, 60, 70, "Shao Kahn was once a servant warrior to Onaga who was once the ruler of Outworld. But in great defiance Kahn turned on Onaga and usurped the throne of the realm. After ousting Onaga from Outworld, he continues with the conquest that Onaga had left behind. He began with lesser realms such as Zaterra and Vaeternus. Then, the Elder Gods insisted that Kahn should only conquer a realm through a martial arts tournament known as Mortal Kombat. Only if Kahn's forces win 10 consecutive Mortal Kombat Tournaments should he conquer a realm. Kahn's forces win one tournament after another and conquered the realms including the gorgeous realm of Edenia where he kills King Jerod and takes Jerod's wife Sindel as his own wife and takes in the infant Kitana and raises her as her personal assassin. As Kahn has taken Edenia, he sets his sights on the last kownn realm, Earthrealm. Kahn's lead scorcerer Shang Tsung was made the tournament's originator and sponsor Outworld in Mortal Kombat in Earthrealm. Kahn's forces have won 9 consecutive Mortal Kombat Tournaments with the help of Shokan warrior Goro who has defeated the shaolin monk Kung Lao. ")

baraka =  Outworld_Fighter("Baraka",110, 1100, 70, 60, "Baraka was introduced as a mean, frightening, and unpredictable Outworld warrior in service of Emperor Shao Kahn in Mortal Kombat II. He belongs to a race of nomadic mutants, later revealed in Mortal Kombat: Deception to be called Tarkata, who populate the vast wastelands of Outworld. Originally, this race was said to be a crossbreed between Netherrealm demons and Outworlders, but this is no longer canon; it is now claimed that the Tarkatans are a separate race whose realm was conquered and annexed long ago by Shao Kahn. As with all Tarkatans, Baraka is cannabalistic and possesses long, retractable blades extending from his forearms, making him one of the most deadly fighters in the Mortal Kombat universe. ")

quan_chi = Netherrealm_Fighter("Quan Chi",100, 1200, 80, 50, "Quan Chi is considered one of the most powerful scorcerers in all of the Realms. Though his true origins are unknown, but some sources say that he is from the Netherealm. 2 years before the 10th generation Mortal Kombat in Earthrealm Quan Chi has begun his quest for an ancient relic known as the \"Sacred Amulet\" which is supposed to re-animate dead beings. This began during a huge war between 2 ninja clans that was obscured from the rest of Earthrealm, a Chinese clan known as \"Lin Kuei\" and a Japanese clan known as \"Shirai-Ryu\", eventually the Lin Kuei won over the Shirai-Ryu with the aid of an assassin known as Sub-Zero (Bi-Han). This is when Quan Chi recruited Bi-Han to help him obtain the Amulet as the map to the relic's precise location which is in the Shaolin Temples, Quan Chi also recruited the last surviving Shirai-Ryu member named Hanzo Hasashi to obtain the map just in case Bi-Han fails, but the 2 ninjas met at the map's location, true to the saying of the Lin Kuei, Bi-Han challenged Hanzo to Mortal Kombat, Bi-Han killed Hanzo and takes the map. As Bi-Han fights and defeats the elemental gods in the temple of the Amulet, he was met by Quan Chi and delivered the Amulet. Then, Quan Chi shows his true intentions to Bi-Han and escapes to the Netherealm, Bi-Han on the decree of Raiden begins to chase Quan Chi. As Bi-Han ventures to the Netherealm, Quan Chi has done many things, like sending his personal assassin Sareena to find and kill Bi-Han, he also used the amulet to re-animate Hanzo Hasashi, now known as Scorpion and even made a duplicate of the Amulet. Quan Chi eventually has caught up with Bi-Han and challenged him to Mortal Kombat with Bi-Han winning. Though Bi-Han would eventually defeat Quan Chi's proposed master, Shinnok Quan Chi would come up with a contigiency. Bt this would take several more years to come into fruition (in shadow of the events of Mortal Kombat, Shao Kahn's tournament in Outworld and Kahn's invasion of Earthrealm). ")

shinnok = Netherrealm_Fighter("Shinnok",120, 1000, 60, 70, "Shinnok, also known as The Fallen Elder God, is a character in the Mortal Kombat fighting game series. A vengeful, powerful Elder God of Death, he seeks death and destruction across all the realms. He serves as a primary antagonist of the franchise alongside Shao Kahn. ")

noob_saibot = Netherrealm_Fighter("Noob Saibot",110, 1100, 70, 60, "Noob Saibot was originally Sub-Zero in the Mortal Kombat games leading up to Mortal Kombat: Deception before he was murdered by Scorpion in an act of revenge for claiming his life. After his death, Saibot had to prove himself within the Netherealm, and in time, reformed his power to become more deadlier than ever. His family were in allegiance with the Lin Kuei, himself being a high rolling assassin. His father was also part of the clan and was originally from China before he married an American women who gave birth to two sons, and one daughter. However, the boys' father chose to return to china with his two sons, who would eventually take after him as professional assassins. Though neutral, Saibot always had an evil streak after killing in cold blood for so many years. ")

raiden = Marial_Artist_Fighter("Raiden",100, 1200, 80, 50, "Raiden is a God of Thunder and Lightning that is the leading protector of Earthrealm. Though, during a quarrel of the Elder Gods caused by Shinnok who betrayed the other Gods, he helped the Elder Gods banish Shinnok into the Netherrealm for his treachery. But by Doing this, Raiden made earthrealm more vulnerable to a potential invasion by another realm. But this would not come until the present time. ")

liu_kang = Marial_Artist_Fighter("Liu Kang",120, 1000, 60, 70, "Liu Kang is the current elder brother of a sacred Shaolin Temple. Highly trained in the martial arts. It was Liu Kang's destiny to fight in the Mortal Kombat tournament, as the blood of the legendary Kung Lao runs in his veins. He was trained by Outworld warrior Bo' Rai Cho who had taught him the Dragon Kick (which would make Liu Kang a legend someday). As Liu Kang came of age, (like his ancestor) became a member of the sacred Shaolin group known as the White Lotus Society. ")

kung_lao = Marial_Artist_Fighter("Kubg Lao",110, 1100, 70, 60, "Kung Lao was a member of the secret Shaolin temple tribe known as the White Lotus Society. His ancestor, the Great Kung Lao, has competed in several Mortal Kombat tournaments. At one of these tournaments, he faced its champion Shang Tsung. Kung Lao defeated Shang Tsung and was the new champion of Mortal Kombat. As the next generation Mortal Kombat came along, Kung Lao entered to defend his title. Unfortunately, he was defeated by the Shokan Goro, who finished him and Shang Tsung later consumed his soul. 500 years after Kung Lao's death, the Shaolin warrior, Liu Kang entered the 10th generation tournament, and defeated not only the champion Goro, but Shang Tsung as well. With the apparent defeat of Shang Tsung, the Outworld emperor Shao Kahn decided to lure the Earthrealm into a trap in Outworld, which lead to Kung Lao, the last descendant of the Great Kung Lao, joining Raiden in helping the Earthrealm Warriors in their fight against the Outworld's forces. ")

johnny_cage = Spec_Ops_Fighter("Johnny Cage",100, 1200, 80, 50, "Johnny Cage was born of a rich family. Johnny always had a uncanny knack for martial arts, as he was trained by martial arts masters all over the world. He would later use his special talent for movies. He starred in such films like Ninja Mime, Dragon Fist, Massive Strike and Citizen Cage. ")

sonya_blade = Spec_Ops_Fighter("Sonya Blade",120, 1000, 60, 70, "Sonya Blade is a Lieutenant of the United States Army Special Forces. She began her military career by teaming up with Major Jackson Briggs (or Jax) in his mission to bring down the international criminal organization the Black Dragon. On one of these missions, she and a good partner of hers ran ito one of the organizations' members named Kano. During a fight with Kano, he killed Sonya's partner, this would make Kano Sonya's bitter enemy and she will not rest until he is brought to justice by any means necessary. Sonya soon becomes a leader of her own unit that will be dedicated to the apprehention of Kano. ")

jax_briggs = Spec_Ops_Fighter("Jax Briggs",110, 1100, 70, 60, "Major Jackson Briggs is one of the toughest units in the Special Forces. He receives a distress call from Gemini telling him that there was a prison break and several members of the Black Dragon such as Tasia, No Face Tremor and Jarek and have went to a place in Chicago. Jax believes that the mastermind behind the prison break was none other than Kano. Jax tracks down the escapees and finds No Face in an abandoned warehouse and defeats him, he then faces Tasia in the sewers and defeats her. Jax then receives word that the Black Dragon took hold of a corporate building and Jax heads there. In the building, he faces Jarek and defeats him. Jarke tells Jax that the last escapee: Tremor is in the lost city of Sinkiang, as Jax defeats Tremor he also finds a portal to Outworld. Where he faces Kano who takes in his possession: The Eye of Chitian which has strong magic. Jax defeats Kano and takes the artifact with him. ")
