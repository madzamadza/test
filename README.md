Teorijski deo
---

Dati sto konciznije odgvore u formi prosto prosirenih recenica na svako od sledecih pitanja.

01. Sta je to JSON?
Java Script Object Notation je sintaksa za razmenu podataka i njihovo slaganje.
02. Sta je to XML?
Extensible Markup Language je jezik sa unapred određenim skupom tagova. Meta jezik koji se koristi zadefinisanje drugih jezika.
03. Sta je to URL?
Uniform Resource Link njime se definiše svaki resurs na vebu.
04. Sta je to HTTP?
Hypertext Transfer Protocol - stranice na vebu se razmenjuju putem protokola. Jedan od njih je http.
05. Sta je to RESTful API?
RESTful API  je aplikacija koja izvršava http rikvestove kako bi izvršila metode get, push, post i delete. 
06. Koje HTTP metode imamo?
Get, Head, Patch, Connect, Post, Put, Trace, Options, Delete
07. Sta je to DNS?
Domain Name Server - daje računaru IP adresu.
08. Sta je to private IP?
Privatna IP adresa koja se koristi za internu upotrebu i nije javna.
09. Sta je to AJAX?
Čita podatke sa servera kada je strana loudovana, ažurira veb stranu bez rifrešovanja i menja podatke u pozadini.
10. Sta je to TCP/IP?
Skup protokola koji omogućava umreženim računarima da dele resurse putem mreže.
11. Sta je to kes memorija?
Keš memorija je memorija koja služi za zapis podataka koji se često koriste. Obično je mala. 
12. Koja je razlika izmedju klase i objekta?
Klasa (class) je šablon na osnovu koga se kreira objekat, dok objekat (object) postoji u trenutku izvršavanja programa (runtime). Razliku je najbolje opisati kroz primer a person (klasa) i the person (objekat).

Backend
---

1. U `models.py` fajlu implementirati `Comment` model (klasu) u Python-u koja sadrzi atribute:
- `text`: sam komentar, i
- `date`: datum komentara u formatu `YYYY-MM-DD`
"Override"-ovati `__repr__` metod.

2. U `models.py` fajlu definisati `COMMENTS` varijablu koja sadrzi niz od 3 elementa koji su tipa `Comment`. 

3. U `app.py` fajlu napraviti Flask applikaciju koja ima `index` "view" funkciju koja handle-uje `/` route. Funkcija bi trebalo da vraca HTML string koji u `body`-ju sadrzi heading "Welcome!".

4. U `app.py` dodati `comments` "view" funkciju koja handle-uje `/comments` route. Funkcija bi trebalo da vraca HTML koji u `body`-ju sadrzi tabelu komentara. Koristiti Flask template.

5.  U `app.py` dodati `api_comments` "view" funkciju koja handle-uje `/api/v1.0/comments` route. Funkcija bi trebalo da vraca JSON reprezentaciju `COMMENTS` niza.

Frontend
---

U `home.html` fajlu imlementirati jednostavnu klijent aplikaciju kojom moze da testira prethodno implementirani API end point. Koristiti `form` i `iframe`.

Algoritmi
---

Napisati i JavaScript i Python funkciju koja predstavlja resenje sledeceg zadataka:

Write a program that prints the numbers from 1 to 100. But for multiples of three print `Fizz` instead of the number and for the multiples of five print `Buzz`. For numbers which are multiples of both three and five print `FizzBuzz`.

JS
for( var i=1; i<101; i++ ) {
    if( (i%3) === 0 && (i%5) === 0 ) {
        console.log( "FizzBuzz" );
    }else if( (i%3) === 0 ) {
        console.log( "Fizz" );
    }else if( (i%5) === 0 ) {
        console.log( "Buzz" );
    }else{
        console.log( i );
    }
}

Python
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)

print "\n".join(fizzbuzz(n) for n in xrange(1, 101))

Uputstvo
---

Resenja i odgovore predati u okviru GitHub repozitorijuma.