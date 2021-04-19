from rich.console import Console
from rich.theme import Theme
#~		~#

#~
ipurpleu = Theme({
	"text": "#F5EDFF",
	"info": "#C89EFF",
	"warning": "#D9BAFF",
	"danger": "#7E5AAD"
})
#~

console = Console(theme=ipurpleu)

if __name__ == '__main__':
	console.print("[text]Testing colors...")
	console.print("[text]TEXT text TeXt [white]- #F5EDFF")
	console.print("[info]INFO info InFo [white]- #C89EFF")
	console.print("[warning]WARNING warning WaRnInG [white]- #D9BAFF")
	console.print("[danger]DANGER danger DaNgEr [white]- #7E5AAD")