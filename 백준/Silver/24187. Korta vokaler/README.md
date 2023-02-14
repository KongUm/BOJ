# [Silver I] Korta vokaler - 24187 

[문제 링크](https://www.acmicpc.net/problem/24187) 

### 성능 요약

메모리: 113112 KB, 시간: 120 ms

### 분류

다이나믹 프로그래밍(dp), 문자열(string)

### 문제 설명

<p>Att lösa algoritmproblem är svårt, men en sak som ofta är ännu svårare är att förbereda testdatan. Ta problemet <em>Arabiska</em> till exempel. Här har juryn lagt många timmars intensivt arbete åt att konstruera mästerverk som <code>hej vad heter du</code>.</p>

<p>En fråga som dyker upp är: hur skapar man textsträngar som inte innehåller några korta vokaler? Om du läste uppgiften <em>Arabiska</em> så kanske du kommer ihåg att en kort vokal är en vokal som följs av minst två konsonanter. I ordet <code>tall</code> så är a:et en kort vokal, medan ordet <code>potatis</code> inte har några korta vokaler. För enkelhets skull räknar vi  <em>a, e, i, o, u, y</em> som vokaler i det här problemet.</p>

<p>Ett sätt att skapa ord som inte innehåller några korta vokaler är att utgå ifrån ett ord, och sedan ta bort några bokstäver från det. Om vi utgår från <code>potatis</code> så skulle vi då kunna få <code>ptais</code> till exempel. Men om ordet istället blev <code>otats</code> så uppstod tyvärr en kort vokal.</p>

<p>Din uppgift är att räkna antalet sätt att ta bort bokstäver från ett givet ord så att resultatet inte innehåller några korta vokaler. Det är tillåtet att inte ta bort några bokstäver alls (i andra exemplet så bidrar det med $1$ till svaret). Däremot är det inte tillåtet att ta bort alla bokstäver. Om samma ord uppstår genom att ta bort olika mängder bokstäver, så räknas de separat (I första exemplet finns det två sätt att få ordet <code>tal</code>, vi kan ta bort det första eller det andra <code>l</code>:et).</p>

### 입력 

 <p>Indatan består av en rad med ett ord $S$ med högst $50$ bokstäver. Ordet består bara av bokstäverna <code>a-z</code>.</p>

### 출력 

 <p>Skriv ut ett heltal, antalet sätt att ta bort bokstäver så att ett ord utan korta vokaler bildas.</p>

<p>Notera att svaret inte alltid får plats i ett $32$-bitars heltal i de senare testfallen.</p>

