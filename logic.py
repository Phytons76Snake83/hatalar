import aiohttp  # Eşzamansız HTTP istekleri için bir kütüphane
import random
import main
from datetime import datetime, timedelta


class Pokemon:
    pokemons = {}
    # Nesne başlatma (kurucu)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1025)
        self.name = None
        self.hp = None
        self.power=None
        self.super_power=None
        self.feed = None
        if pokemon_trainer not in Pokemon.pokemons:
            Pokemon.pokemons[pokemon_trainer] = self
        else:
            self = Pokemon.pokemons[pokemon_trainer]
        self.last_feed_time = datetime.now()
    async def get_name(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için eşzamansız bir yöntem
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data['forms'][0]['name']  # Bir Pokémon'un adını döndürme
                else:
                    return "pokeball"  # İstek başarısız olursa varsayılan adı döndürür
    
    
    async def get_hp(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için eşzamansız bir yöntem
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data['stats'][0]['base_stat']  # Bir Pokémon'un adını döndürme
                else:
                    return 1 # İstek başarısız olursa varsayılan adı döndürür
                
    async def get_power(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için eşzamansız bir yöntem
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data['stats'][1]['base_stat']  # Bir Pokémon'un adını döndürme
                else:
                    return 0  # İstek başarısız olursa varsayılan adı döndürür   
                
    async def get_super_power(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için eşzamansız bir yöntem
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data['stats'][3]['base_stat']  # Bir Pokémon'un adını döndürme
                else:
                    return 0  # İstek başarısız olursa varsayılan adı döndürür   
    async def info(self):
        # Pokémon hakkında bilgi döndüren bir metot
        if not self.name:
            self.name = await self.get_name()  # Henüz yüklenmemişse bir adın geri alınması
        
        if not self.hp:
            self.hp = await self.get_hp()  # Henüz yüklenmemişse bir adın geri alınması
        

        if not self.power:
            self.power = await self.get_power()  # Henüz yüklenmemişse bir adın geri alınması
        return f"Pokémonunuzun ismi: {self.name} \n Pokémonunuzun sağlığı: {self.hp} \n  Pokémonunuzun gücü: {self.power} "


    async def show_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data["sprites"]["other"]["official-artwork"]["front_default"]
                else:
                    return None

    async def attack(self, enemy):
          
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Pokémon eğitmeni @{self.pokemon_trainer} @{enemy.pokemon_trainer}'ne saldırdı\n@{enemy.pokemon_trainer}'nin sağlık durumu {enemy.hp}"
        else:
            enemy.hp = 0
            
            del Pokemon.pokemons[enemy.pokemon_trainer]
          
            return f"Pokémon eğitmeni @{self.pokemon_trainer} @{enemy.pokemon_trainer}'ni yendi!" 

    async def feed(self, feed_interval=20 , hp_increase=10):
        current_time=datetime.now
        delta_time = timedelta(seconds=feed_interval)
        if (current_time - self.last_feed_time)>delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Pokemonun sağlığı arttı. Mevcut sağlık {self.hp}"
        else:
            return f"pokemonunuzu şu zaman besleyebilirsiniz {current_time + delta_time}"

        



