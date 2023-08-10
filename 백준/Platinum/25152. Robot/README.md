# [Platinum II] Robot - 25152 

[문제 링크](https://www.acmicpc.net/problem/25152) 

### 성능 요약

메모리: 115268 KB, 시간: 132 ms

### 분류

비트마스킹, 해 구성하기

### 문제 설명

<p>Krešo se voli igrati sa svojim robotom. Za robota voli konstruirati labirint i onda pratiti kako se robot kreće po njemu.</p>

<p>On robota postavi u gornji lijevi kut labirinta koji je predstavljen kao ploča s R redaka i S stupaca. Neka polja labirinta su blokirana. Robot se u svakom trenutku može pomaknuti na polje koje se nalazi desno ili dolje od trenutnog polja. Ako je to polje blokirano, robot se na njega ne može pomaknuti. Igra završava kada robot stigne u donji desni kut labirinta.</p>

<p>Krešo želi konstruirati labirint koji će biti dovoljno težak tako da robotu igra bude zanimljiva. Preciznije, Krešo želi da njegov labirint ima točno K različitih puteva kojima se robot može kretati u igri. Pomozi Kreši konstruirati takav labirint.</p>

<p>Napomene: Krešo može sam odabrati dimenzije labirinta, ali one moraju biti manje ili jednake od 1000.</p>

<p>Dva puta smatramo različitima ako postoji polje kroz koje je robot prošao u jednom putu, ali nije u drugom.</p>

<p>Robot igru počinje na polju koje pripada prvom retku i prvom stupcu, a završava na polju koje pripada zadnjem retku i zadnjem stupcu. Nije dozvoljeno blokirati nijedno od tih dvaju polja.</p>

### 입력 

 <p>U prvom i jedinom retku nalazi se prirodan broj K (1 ≤ K ≤ 1 000 000 000).</p>

### 출력 

 <p>U prvi redak ispiši dimenzije labirinta R, S (1 ≤ R, S ≤ 1 000).</p>

<p>U svakom od sljedećih R redaka ispiši S znakova ‘0’ ili ‘1’. Ovih R x S znakova opisuju Krešin labirint.</p>

<p>Znak ‘1’ označava da je odgovarajuće polje blokirano, a ‘0’ da je slobodno.</p>

