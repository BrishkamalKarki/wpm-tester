from colorama import Fore,Style
import time
from anime_inf import inf_ani

print(Fore.LIGHTYELLOW_EX,"-------------------------------------------------------------------------------------",Style.RESET_ALL)
print(Fore.GREEN,inf_ani(),Style.RESET_ALL)

print(Fore.LIGHTMAGENTA_EX,"-------------------------------------------------------------------------------------",Style.RESET_ALL)

print(Fore.YELLOW,"Press 'Enter' and Copy the shown paragraphs" ,Style.RESET_ALL)
input()



print(Fore.LIGHTBLACK_EX,"-------------------------------------------------------------------------------------\n\n-->",Style.RESET_ALL,end="")

start_time:time=time.time()
user_paragraph:str=input()
end_time:time=time.time()

print(Fore.LIGHTRED_EX,"-------------------------------------------------------------------------------------",Style.RESET_ALL)

user_paragraph:list=list(user_paragraph)
ttl_time_min: float=(end_time-start_time)/60

print(f"The average typing speed is {int((len(user_paragraph)/5)/ttl_time_min)} WPM.")

print(Fore.RED,"-------------------------------------------------------------------------------------",Style.RESET_ALL)

