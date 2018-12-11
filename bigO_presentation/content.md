## Big O: Code Complexity as data grows
**Write Better Code Using Python**
#### Yunindyo Prabowo   
notes:
- pembahasan ini akan bikin pusing hahaha
- pendekatan matematis dan pendekatan pragmatis

---

### Yunindyo Prabowo
---

- **profesi**: Mahasiswa 
- **email**: yunindyo.prabowo@gmail.com
- **blog**: ypraw.gitlab.io
- **github/gitlab**: @ypraw


---

## Introduction design and algorithm analysis

--

### Apa itu Algoritma?

> Algoritma merupakan langkah-langkah (Prosedur) yang harus dilakukan untuk menyelesaikan suatu masalah <!--.element: class="fragment" data-fragment-index="1" -->
notes:
- dalam mendefinisikan sebuah algoritma yg baik ada beberapa hal yang di pertimbangkan.

--

#### Masalah
> yaitu sebuah persoalan yang ingin diselesaikan oleh sebuah algoritma.
<!--.element: class="fragment" data-fragment-index="1" -->

--

#### Masukan (input)
> yaitu contoh data atau keadaan yang menjadi permasalahan.
<!--.element: class="fragment" data-fragment-index="1" -->

--

#### keluaran (output)
> yaitu bentuk akhir dari data atau keadaan setelah algoritma diimplementasikan ke masukan. Keluaran merupakan hasil ideal yang diinginkan dan dianggap telah menyelesaikan masalah.
<!--.element: class="fragment" data-fragment-index="1" -->

---

## Algoritma yang Baik

notes:
- tentu dalam menyusun algoritma yang baik di pengaruhi oleh beberapa criteria

--

### Benar
>  di mana algoritma menyelesaikan masalah dengan tepat, sesuai dengan definisi masukan / keluaran algoritma yang diberikan. <!--.element: class="fragment" data-fragment-index="1" -->

--

### Efisien
> berarti algoritma menyelesaikan masalah tanpa memberatkan bagian lain dari apliikasi. Sebuah algoritma yang tidak efisien akan menggunakan sumber daya (memori, CPU) yang besar dan memberatkan aplikasi yang mengimplementasikan algoritma tersebut <!--.element: class="fragment" data-fragment-index="1" -->

--

### Mudah di Implementasikan
> artinya sebuah algoritma yang baik harus dapat dimengerti dengan mudah sehingga implementasi algoritma dapat dilakukan siapapun dengan pendidikan yang tepat, dalam waktu yang masuk akal.
<!--.element: class="fragment" data-fragment-index="1" -->

---

### Realita ???



![img](images/ga_mudah.jpg)
<!--.element: class="fragment" data-fragment-index="1" -->




---

### Big O : Asymptotic Notation for Complexity Analysis of Algorithms

---

### Definition &amp; Terminology
- O <!-- .element: class="fragment" data-fragment-index="1" --> ``` => stand for Order Of``` <!-- .element: class="fragment" data-fragment-index="2" --> 
- bla bla bla N <!-- .element: class="fragment" data-fragment-index="3" --> ```=> Banyaknya data``` <!--.element: class="fragment" data-fragment-index="4" -->

- <!--.element: class="fragment" data-fragment-index="5" --> O(N), O(log n) etc.

- not running time measure <!--.element: class="fragment" data-fragment-index="6" -->

- given 10 times data, how much time to finish??? <!--.element: class="fragment" data-fragment-index="7" -->

notes: 
- bukan mengukur seberapa cepat kode di kompilasi
- bukan mengukur seberapa banyak aksi dalam sekali running
- tapi mengukur seberapa lambatnya kode yang kita buat ketika data itu berkembang menjadi lebih banyak dari yang sebelum-sebelumnya 


--

### Examples

--

### contoh 1 

```python
def pangkat(x, y):
    hasil = 1
    for i in range(0, y):
        hasil = x * hasil
    return hasil
```
notes:
- pada dasarnya fungsi diatas menjalankan x sebanyak y kali dengan operasi perkalian.
- seberapa efisien algoritma ini???
- berapa hasilnya?

--

### pembahasan contoh 1
<!-- .element: class="fragment" data-fragment-index="2" -->

```python
pangkat(2,3)
``` 
<!-- .element: class="fragment" data-fragment-index="1" -->

```python
hasil = 1           # iterasi ke 0 hasil =1
```
<!-- .element: class="fragment" data-fragment-index="3" -->

```python
hasil = 2 * hasil   # iterasi ke 1 hasil = 2
```
<!-- .element: class="fragment" data-fragment-index="4" -->

```python
hasil = 2 * hasil   # iterasi ke 2 hasil = 4
```
<!-- .element: class="fragment" data-fragment-index="5" -->

```python
hasil = 2 * hasil   # iterasi ke 3 hasil = 8
```
<!-- .element: class="fragment" data-fragment-index="6" -->

>    ```python
>    return hasil 
>    ```
<!-- .element: class="fragment" data-fragment-index="7" -->

--

### pembahasan contoh 1 (lanj)

| Baris Kode        | Jumlah eksekusi |
| :---              | :---- |
| hasil = 1         |  1    |
| hasil= x * hasil  | y     |
| return hasil      | 1     |

> dalam kata lain bahwa fungsi pangkat ini akan selalu di eksekusi sebanyak 2 + y atau bisa disederhanakan menjadi O(y) atau O(N) bigO Linier.
<!-- .element: class="fragment" data-fragment-index="8" -->

notes:
- bayangkan jika eksekusinya menjadi N kuadrat ???
- butuh berapa lama eksekusinya ??
- dapatkah di sederhakan fungsi diatas??? let's code here ...