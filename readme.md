# Game of GO
### #A18
### Calcan Teodor Alexandru

- Interfață grafică minimală pentur un joc de GO.
- Opțiunea de a juca în doi sau cu mutările aleatoare ale calculatorului.

## Funcții

> ```class Tura```:
> - `def __init__(self, grid_size, player)`: Inițializează clasa cu un `np.array` de zero, de dimensiunea `grid_size-1` * `grid_size-1`, și identifică primul player (piese de culoarea neagră) printr-un *1*.
> - `def next(self, i, j)`: Creează următoarea stare/tură folosind un `i` și un `j` pentru a identifica poziția piesei plasată. `self.player` indică playerul și culoarea piesei. Prin `self.checkCaptures()` se identifică piesele capturate. `print(self.scores)` afișează scorul curent, după ce au fost executate capturile de piese. Playerul este schimbat la final.
> - `def pas(self)`: Reprezintă abținerea de la mutare. Playerul se schimbă.
> - `def checkGroupLib(self, playerGroups)`: Verifică libertățile grupurilor unui player și le elimină pe cele cu 0 libertăți.
> - `def checkPointLib(self, i, j)`: Verifică libertățile unui punct singular în funcție de `i` și `j`.
> - `def checkPointLibGroup(self, i, j)`: Verifică libertățile unui punct dintr-un grup în funcție de `i` și `j`.
> - `def checkCaptures(self)`: Elimină punctele singulare capturate într-o tură, folosindu-se de `self.grid` și de `checkPointLib`.
> - `def checkGroups(self)`: Construiește grupurile (insulițele) de piese de pe tablă pentru ambii jucători.

> `Globale`:
> - `def checkPointLibGb(grid, i, j)`: Aceeași funcționalitate ca `checkPointLib`, dar în context global.
> - `def checkMove(tura: Tura, i, j)`: Verifică dacă o mutare este corectă din punct de vedere al regulilor jocului, înainte ca aceasta să fie efectuată.
> - `def drawGrid(i: int, tura: Tura)`: Funcția apelată constant de `pygame` pentru a desena pe ecran tabela de joc și piesele aflate pe tablă.
> - `def draw_window()`: Funcția apelată de `pygame` pentru a desena pe ecran elementele care vor rămâne constante de-a lungul jocului.
> - `def getPosition()`: Funcția folosită pentru a deduce poziția unde playerul vrea să așeze piesa din coordonatele cursorului. După ce coordonatele sunt identificate și mutarea este verificată, se apelează `tura.next()`.
> - `def computerMove()`: Calculatorul generează coordonate random `i` și `j` până obține o mutare validă, urmând ca `tura.next()` să fie apelată.

> Librării folosite:
> - `pygame`
> - `numpy`
> - `sys`
> - `random`