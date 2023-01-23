<h1>System automatycznej estymacji poziomu wody w rzece</h1>
<h3>Opis</h3>
<ul>
  <h4>Cel</h4>
  Stworzenie modelu/algorytmu, który na bazie danych historycznych oraz prognozy pogody, pochodzących z IMGW, pozwoli prognozować poziom wody rzeki. 
  <h4Realizacja</h4>
  Ideą przyświiecającą zespołowi ObjectNotFound było wykorzystanie sieci neuronowych do przewidywania poziomu wody w rzece. Dane postanowiliśmy zapisywac w bazie danych Oracle, która jest bardzo wydajna. Wykorzystana architektura oraz wykonanie interfejsu graficznego w formie aplikacji internetowej sprawia, że system jest dostępny dla wszystkich osób w obrębie sieci oraz będzie działać na każdym urządzenie niezależnie od systemu operacyjnego czy typu. 
</ul>  
<h3>Wymagania funkcjonalne</h3>
<ul>
  System będzie automatycznie prognozować poziom wody w rzece na podstawie danych historycznych oraz prognozy pogody pochodzącej z IMGW.
</ul>
<ul>
  System będzie zbierał dane historyczne dotyczące poziomu wody w rzece oraz prognozy pogody z IMGW.
</ul>
<ul>
  System będzie posiadał interfejs użytkownika pozwalający na przeglądanie prognozowanego poziomu wody w rzece oraz danych historycznych.
</ul>
<ul>
  System będzie posiadał funkcję alarmową, która poinformuje użytkownika o przekroczeniu prognozowanego poziomu wody w rzece.
</ul>
<ul>
  System będzie zintegrowany z systemami hydrotechnicznymi Zakładu Hydrotechnicznego, umożliwiając automatyczne dostosowanie planów gospodarki wodnej.
</ul>
<h3>Wymagania niefunkcjonalne</h3>
<ul>
  System będzie dostępny 24/7 z nie więcej niż 2% przerw w działaniu.
</ul>
<ul>
  System będzie wykazywał czas odpowiedzi na poziomie mniejszym niż 5 sekund dla żądania prognozy poziomu wody.
</ul>
<ul>
  System będzie skalowalny i będzie mógł obsługiwać rosnące wymagania dotyczące ilości danych i użytkowników.
</ul>
<ul>
  System będzie zgodny z normami branżowymi dotyczącymi gospodarki wodnej i bezpieczeństwa.
</ul>
<h3>Przypadki użycia</h3>
<ul>
  <table>
    <tr>
      <th>Nazwa</th>
      <th>Działanie</th>
    </tr>
    <tbody>
      <tr>
        <th>Prognozowanie poziomu wody</th>
        <td>Użytkownik wprowadza datę, na którą chce uzyskać prognozę poziomu wody w rzece. System automatycznie generuje prognozę na podstawie danych historycznych oraz prognozy pogody z IMGW.</td>
      </tr>
      <tr>
        <th>Przeglądanie danych historycznych</th>
        <td>Użytkownik może przeglądać dane historyczne dotyczące poziomu wody w rzece w określonym przedziale czasowym.</td>
      </tr>
      <tr>
        <th>Ustawienie alarmu</th>
        <td>Użytkownik może ustawić alarm, który poinformuje go o przekroczeniu prognozowanego poziomu wody w rzece.</td>
      </tr>
      <tr>
        <th>Integracja z systemami hydrotechnicznymi</th>
        <td>Użytkownik może zintegrować system z systemami hydrotechnicznymi Zakładu Hydrotechnicznego, aby automatycznie dostosować plany gospodarki wodnej.</td>
      </tr>
    </tbody>
  </table>

  <h4>Diagram przypadków użycia</h4>
  <ul>
    <img src="https://user-images.githubusercontent.com/68614570/214142786-a0daeefe-6b99-45c4-a08a-9037775f988f.jpg" width="500" height="333" alt="214142786-a0daeefe-6b99-45c4-a08a-9037775f988f">
  </ul>
</ul>
