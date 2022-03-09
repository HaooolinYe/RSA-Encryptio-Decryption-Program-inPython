<h1 id="opener"> RSA-Encryptio-Decryption-Program-inPython <img src="https://user-images.githubusercontent.com/90864900/157359880-1c55654d-7b1f-45e5-9494-e9035d6d09ba.png" width=50 height=50></h1>
A <em>Python program</em> that is able to do <em>RSA encryption</em> and <em>decryption</em>. A valid message to be encrypted or an output decrypted meessage could contain any of the <strong>26 English alphabets</strong> and the <strong>common puncutation marks</strong>.

<p align="center">
<img src="https://user-images.githubusercontent.com/90864900/157359529-76ad4562-befc-4b65-9f72-43342c320bd6.png" height=400 width=700>
</p>

<h2 id="gd"> Guide </h2>
<ul>
  <li><strong><a href="#py">Python Installation</a></strong></li>
  <li><a href="#menu">
    <strong>Menu</strong></a>
    <ol>
      <li><a href="#bob">Encryption</a></li>
      <li><a href="#alice">Decryption</a></li>
    </ol>
  </li>
  <li><strong><a href="#math">Handy Maths Concepts</a></strong>
      <ol>
        <li><a href="#ascci">Self-made ASCCI table</a></li>
        <li><a href="#sqrt">Find Prime through √</a></li>
        <li> <a href="#euclidean">Euclidean Algorithm</a></li>
      <!--<li> Inverse in Modulo </li>-->
    </ol>
  </li>
</ul>

<h2 id="py"> Python Installation <img src="https://user-images.githubusercontent.com/90864900/157484639-967287e1-87ba-426c-99a7-9733f9aea50f.png" width=25 height=25>
</h2>
<p>
  If you are new to Python, then here's some steps you could follow to get started with setting it up on your PC.
  <br>
  Short path to get Python on your PC is to download < a href="https://thonny.org/">Thonny</a>. This is really a beginner friendly IDE. Python is attached with Thonny, so once you have Thonny on your PC, you can run any .py program on it.
  <br>
  To my Linux friends, the following commands can install Thonny/Python on your device:
  <br>
  <dl>
    <dt>
  <em>Raspbian</em>
    </dt>
  <dd>
    
  ```
  sudo apt install thonny
  ```
    
  </dd>
  <dt>
    <em>Debian</em>
    </dt>
  <dd>
    
  ```
  sudo apt install python3-tk thonny
  ```
    
  </dd>
  <dt>
    <em>Ubuntu</em>
  </dt>
  <dd>
    
  ```
  sudo apt install python3-tk thonny
  ```
    
  </dd>
  <dt>
    <em>Fedora</em>
  </dt>
  <dd>
    
  ```
  sudo dnf install python3-tkinter thonny
  ```
    
  </dd>
    
 </dl>
<i> Keke... Now we should be ready to jumpy into the pool of Python and RSA :D</i>
<p align="right"><a href="#gd">↑Top</a></p>
</p>

<h2 id="menu"> Menu <img src="https://user-images.githubusercontent.com/90864900/157484501-b2667b25-1bb8-45e7-8a76-c982f448a236.png" width=25 height=25>
</h2>
In this chapter, I am going to explain to you the two main functions of this program. Before that, let me introduce you two best friends: <em>Alice👧</em> and <em>Bob👦</em>.
<br>
Bob sometimes tells Alice little <em>secretes</em>, and he obviously <strong>doesn't want</strong> anyone else to know what those secrets are. Therefore, Bob invented an encoding method. He would first encrypted the secret, which is in English and may contain some puncutation marks, into <em>a list of inegers</em> and send it and some <strong>private and public keys</strong> to Alice. The keys are going to help Alice to decrypt that integer list back to human readable languages. <i>(Notice, even if other people know what the public key is, he/she won't be able to decrypt the message. If that person has all the keys, the decryption still cannot be done without the knowledge of RSA.)</i>
<p align="right"><a href="#gd">↑Top</a></p>

---------------------------------------------------------------------------
<h3 id="bob"> Bob 👦</h3>
<p>
  As <i>"Bob"</i>, you would need to decide what <i><strong>k</strong></i> and <i><strong>m</strong></i> are.
  <br>
  <dl>
    <dt>k:</<dt>
    <dd> A public key, needs to be <strong>a prime number!</strong> Usually, the bigger the k is , the safer your encryption would be.</dd>
        <dt>m:</<dt>
    <dd> A product of two prime number. Again, the bigger, the better</dd>
    </dl>
  Don't worry if you are afraid the numbers you entered are not prime. We have an <em>auto-checker</em> that checks whether the number is prime or not. This checker uses <em>the square-root prime check method</em>.
  <br>
  Then, just enter the message you wish to be encrypted, and the program will output it for you:).
<img src="https://user-images.githubusercontent.com/90864900/157482435-510f1676-3795-4aeb-96f9-d5bbbedafd2f.png">
<p align="right"><a href="#gd">↑Top</a></p>
</p>

---------------------------------------------------------------------------

<h3 id="alice"> Alice 👧</h3>
<p>
  As <i>"Bob"</i>, you would use the keys that <em>Bob 👦</em>sent to you to decrypt the integer message.
  <br>
  The keys are:
    <dl>
    <dt>k:</<dt>
      <dd> A public key. It needs to be a <em>Prime</em></dd>
    <dt>p:</<dt>
      <dd>m is a product of <em>two prime numbers</em>, and p is one of the prime.</dd>
    <dt>q:</<dt>
    <dd>p*q = m.</dd>
    <dt>integer message:</<dt>
    <dd>This is the decrypted message that Bob 👦 sent to you. It has type string, but separated by a blank space. Therefore, we can treat it as a list.</dd>
    </dl>
 <i>Again, we have a prime checker to verify if the numbers you entered are prime if it's necessary for them to be;)</i>
 <br>
 Then, after giving the prorgam all of these, you can just wait for the program to output you the decrypted message!
 <img src="https://user-images.githubusercontent.com/90864900/157482671-225cb890-33ee-42fd-9bcb-10ebfb370316.png">
 <i>Notice, the output message are all in capital letters, while the origional message are not. This can be easily fixed later on when we talk about out own <a href="#ascci"<strong><em>ASCCI table</em></strong></a> :)</i>
 <p align="right"><a href="#gd">↑Top</a></p>
</p>

<h2 id="math"> Maths <img src="https://user-images.githubusercontent.com/90864900/157484212-364147ac-cc05-494d-8587-2b84ab3a16f5.png" height=20 width=20> </h2>
<p>If you are not familiar with how RSA works. Continuing reading <em>is not recommanded!!!</em> The following chunks are the implementations of those methematical theorems and algorithms in the modern computer programming languages, <em>not for a teaching purpose</em>.
  <br> If you survive from the warning above,let's list some of the handy maths strategies we used in this program:D</p>

---------------------------------------------------------------------------
<h3 id="ascci">Self-made ASCCI table</h3>
<p> To encrypt the English message to integers, we have an ASCCI Table which has the 26 alphet Capital letters and punctuation marks with their corresponding numbers.
  <table align="center" cellpadding="15" width="100%">
    <tr>
<th>A</th>
<th>B</th>
<th>C</th>
<th>D</th>
<th>E</th>
<th>F</th>
<th>G</th>
<th>H</th>
<th>I</th>
<th>J</th>
<th>K</th>
<th>L</th>
<th>M</th>
<th>N</th>
<th>O</th>
<th>P</th>
<th>Q</th>
<th>R</th>
<th>S</th>
<th>T</th>
<th>U</th>
<th>V</th>
<th>W</th>
<th>X</th>
<th>Y</th>
<th>Z</th>
<th> </th>
<th>!</th>
<th>,</th>
<th>.</th>
<th>:</th>
<th>;</th>
<th>'</th>
<th>"</th>
<th>?</th>
    </tr>
    <tr>
<th>12</th>
<th>13</th>
<th>14</th>
<th>15</th>
<th>16</th>
<th>17</th>
<th>18</th>
<th>19</th>
<th>20</th>
<th>21</th>
<th>22</th>
<th>23</th>
<th>24</th>
<th>25</th>
<th>26</th>
<th>27</th>
<th>28</th>
      <th>29</th>
<th>30</th>
<th>31</th>
<th>32</th>
<th>33</th>
<th>34</th>
<th>35</th>
<th>36</th>
<th>37</th>
<th>38</th>
<th>39</th>
<th>40</th>
<th>41</th>
<th>42</th>
<th>43</th>
<th>44</th>
<th>45</th>
<th>46</th>
    </tr>
</table>
This table can be very flexible. That is, you can add any alphbets or symbols you'd like to encrypt to this table, and the program will deal with the maths for you;)
 <p align="right"><a href="#gd">↑Top</a></p>
</p>

---------------------------------------------------------------------------
<h3 id="sqrt"> Find Prime through √ </h3>
<p>The function would be straight forward once you understand the math behind it. Basically, the naive way to determine whether an integer is prime or not is to loop through all numbers between 1 and n-1 to see whether the division between it and n gives you a <em>0 reminder</em>. Though we can do mod pretty fast in a modern programming language, this is still <strong>pretty slow</strong> since the time complexity is O(n) as we have <em>n-2 numbers to check</em>.
<br>
A quick improvement to this algorithm is to check numbers from 2 to sqrt(n). Now, to understand the reason behind this, think of the largest possible divisor of an integer, say 16. The greatest divisor of it should be 8, but this would be notified when we check if 2 is a divsor of 16, so there is no need to go all the way to 8 after we have checked 2. For number that does not have a small divisor, say 77, the largest divisor is only +4 then its smallest divisor. Therefore we conclude that, if there exist a large first divisor, then the bigger it gets, the closer it gets to the last divisor. Eventually, the first and the last would equal, and since the product of them has to be the number we are looking at, such divisor would be the <strong>square root</strong> of it.
  <br>
  From this, we get a time complexity worst case O(√n). This is kinda rare in computer science, and also slower than O(logn). For sure we can do other tests. for example, using <a href="https://en.wikipedia.org/wiki/Fermat%27s_little_theorem"><em>Fermat's Little Theorem</em></a> and that would be super fast, O(1) on average. However, the downside of it is that it never guarantees that the number is truly a prime, even you do the tests several times with different numbers. It can only tell you that the number is more likely to be a prime, yet, we never know unless we do soemthing else to verify it. But do notice when Fermat's little Theorem tells you a number isn't a prime, that is guaranteed! Good to prevent the user from entering a composite maybe, keke.

 ```
  def ifprime(n):
    '''
        ifprime(n) takes an positive integer and returns
        ture if it is a prime and false if it is not
    '''
    result = True
    for x in range(2,int(n**(1/2))+1):
        if not n%x:
            result = False
            break
    return result 
 ```
  
 <p align="right"><a href="#gd">↑Top</a></p>
</p>
</p>

---------------------------------------------------------------------------
<h3 id="euclidean"> Euclidean Algorithm </h3>
<p>
  <i>The Euclidean algorithm is a way to find the greatest common divisor of two positive integers, a and b.</i>
  <br>
  I am not going to spend too much time in explaining the details of how and why this works. This algorithm is pretty elementry for anyone who took discrete mathematics or basic computer science, and yet, somewhat hard for me,a beginner too, to expain it. What I am going to do is to walk you through an example, and show you the code and the magic;)
  <br>
  </p>
  <pre>
a <- 1701
b <- 3768
do:
 1701  = 0(3768) + 1701 
 3768  = 2(1701) + 366 
 1701  = 4(366) + 237 
 366  = 1(237) + 129 
 237  = 1(129) + 108 
 129  = 1(108) + 21 
 108  = 5(21) + 3 
 21  = 7(3) + 0 
Back Track
 3 = 1(108) + -5(21)
 3 = 1(108) + -5(129-1(108)) =-5(129) + 6(108)
 3 = -5(129) + 6(237-1(129)) =6(237) + -11(129)
 3 = 6(237) + -11(366-1(237)) =-11(366) + 17(237)
 3 = -11(366) + 17(1701-4(366)) =17(1701) + -79(366)
 3 = 17(1701) + -79(3768-2(1701)) =-79(3768) + 175(1701)
 3 = -79(3768) + 175(17010(3768)) =175(1701) + -79(3768)
 result <- "3=175(1701) + -79(3768)"
 print(result)
 DONE
 </pre>
<p> I hope you get a good sense of how this algorithm works. Again, if you are not familiar with this, you shouldn't try to understand what RSA is and why we are using this algorithm. If you just got stuck on how this can be implemented in a modern computer language, I got you <em><a href="https://github.com/HaooolinYe/RSA-Encryptio-Decryption-Program-inPython/blob/main/Ex2%20Euclidean%20algorithm.py">this prorgam</a></em> in Python and hopefully this can help you out!.
  <p align="right"><a href="#gd">↑Top</a></p>
</p>
</p>
