Program do automatycznej obsługi zapisów na rajd.
Program zarządza danymi przez Sheets API w arkuszu google, do którego dane zapisywanych osób wysyła arkusz google.
Program wysyła e-maile z potwierdzeniem dla uczestników oraz raporty do administratora za pomocą Gmail API.

Działanie.
1. Osoby się zgłaszają i nie mają żandego stanu ("")
2. Program pobiera te osoby i zapisuje jako nowe
3. Program wysyła do nowych osób e-mail
4. Program informuje że wysłał do nich e-maile -> RAPORT
5. Program oznacza te osoby jako oczekujące na wpłacenie zaliczki ("REG")
6. Administrator oznacza kto wpłacił zaliczkę ("ZAL")
7. Program pobiera osoby które wpłaciły zaliczkę i wysyła im potwierdzenie
   zapisu
8. Program zmienia ich status na zapisani ("SAV")
9. Program informuje że wysłał tym osobom potwierdzenie zapisu i link do fb -> RAPORT
10. Ja oznaczam ręcznie że osoba została dodana do FB ("OK)
11. Program wysyła raport który zawiera:
   - osoby do których zostało wysłane potwierdzenie rejestracji
   - osoby do których zostało wysłane potwierdzenie zapisu
   - wszystkie osoby które mają wpłacić zaliczkę
   - wszystkie osoby które oczekują na dodanie do fb
