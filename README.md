# <font color="azure"><div align="center"><p>**Image Processing Based Robotic Hand**</p> </div></font>

- The software of the project we developed for the "Teknofest Competition" consist of two base sections.

## <font color="Red">**Image Processing:**</font>
 
- It is aimed to imitate in the prototype by taking the angle between the joints of the hand detected in the image taken from the camera. 


|<font color="White">**Package**</font>|<font color="White">**Version**</font>|
| :---------|:-----:|
| Opencv    |4.7.0.72|
| Numpy     | 1.19.5|
| Mediapipe |0.9.0.1|

- The image received with the **OpenCV** and turned to the *RGB* for the processing with **Mediapipe**. Image that given to the **Mediapipe**, when hand detected, *coordinates will reference points 4 point of the 5 fingers*.

![referans](https://github.com/furkankorlu/Image-Processing-Based-Robotic-Hand/assets/122547302/4d851c23-1b03-44c6-a0dd-24e9853d9a4d)

- By processing the received coordinates, the position of the thumb and the height relations of the fingertips with the palm points are examined, it detects that the fingers are closed without calculating the angle. If the fingers are not closed, it detects the coordinates of these 4 points and the angle made by the joints and prints them on the screen.

![acı](https://github.com/furkankorlu/Image-Processing-Based-Robotic-Hand/assets/122547302/f16c29c5-7ff6-4062-96c8-a6ca6b3169c6)

### **Detected angles are examine in 6 index:**

> **5** *value* ---> **0-30** *degrees* --> **OFF**\
> **4** *value* ---> **30-60** *degrees*\
> **3** *value* ---> **60-90** *degrees*\
> **2** *value* ---> **90-120** *degrees*\
> **1** *value* ---> **120-150** *degrees*\
> **0** *value* ---> **150-180** *degrees* --> **ON**

### **The index value received for each finger is added to the list to be transferred by serial communication:**

> **[** Thumb , Index finger , Middle finger , Ring finger , Little finger **]**

- Sending the created list by averaging it every 5 times, in this way allows the prototype to avoid rapid and sudden changes and to act in real time.

# <font color="azure"><div align="center"><p>**Görüntü İşleme Tabanlı Robotik El**</p> </div></font>

- Teknofest yarışması için geliştirdiğimiz projenin yazılımı 2 temel kısımdan oluşuyor.

## <font color="Red">**Görüntü İşleme:**</font>

- Kameradan alınan görüntüde tespit edilen elin eklemleri arasındaki açının alınarak prototipimizce taklit edilmesi amaçlanmaktadır. 

|<font color="White">**Package**</font>|<font color="White">**Version**</font>|
| :---------|:-----:|
| Opencv    |4.7.0.72|
| Numpy     | 1.19.5|
| Mediapipe |0.9.0.1|

- **OpenCV** aracılığıyla alınan görüntüyü **Mediapipe** ile işlemek için *RGB* ye çevirdik. **Mediapipe’a** verilen görüntüde el tespit edildiğinde *5 parmağın 4 referans noktasının koordinatları alınır*.

![referans](https://github.com/furkankorlu/Image-Processing-Based-Robotic-Hand/assets/122547302/4d851c23-1b03-44c6-a0dd-24e9853d9a4d)

- Alınan koordinatlar işlenerek başparmağının konumu ve parmak uçlarının avuç içi noktalarıyla olan yükseklik ilişkileri incelenerek açı hesaplaması yapılmadan parmakların kapalı olduğunu algılar. Eğer parmaklar kapalı değilse bu 4 noktanın kordinatlarıyla eklemlerin yaptığı açıyı tespit eder ve ekrana yazdırır. 

![acı](https://github.com/furkankorlu/Image-Processing-Based-Robotic-Hand/assets/122547302/f16c29c5-7ff6-4062-96c8-a6ca6b3169c6)

### **Tespit edilen açılar 6 endekste incelenir;**

> **5** *değeri* ---> **0-30** *derece* --> **KAPALI**\
> **4** *değeri* ---> **30-60** *derece*\
> **3** *değeri* ---> **60-90** *derece*\
> **2** *değeri* ---> **90-120** *derece*\
> **1** *değeri* ---> **120-150** *derece*\
> **0** *değeri* ---> **150-180** *derece* --> **AÇIK**

### **Her bir parmak için alınan endeks değeri seri haberleşme ile aktarılacak olan listeye eklenir;**

>**[** Baş , İşaret , Orta , Yüzük , Serçe **]**

- Oluşturulan listenin her 5 defada bir ortalaması alınarak bu şekilde gönderilmesi prototipin hızlı ve ani değişimlerden kaçınmasını ve gerçek zamanlı hareket etmesini sağlar.
