Genetik Algoritmalar ile Problem Çözme

Bu proje, genetik algoritmaların nasıl kullanılabileceğini göstermek için basit bir örnek içerir. Genetik algoritmalar, doğal seçilim ve genetik çaprazlama gibi biyolojik evrimden ilham alan optimizasyon algoritmalarıdır.

Matematiksel Fonksiyonlar:
- Uygunluk Fonksiyonu: Her bireyin uygunluk değerini hesaplar. Bu örnekte, bireylerin toplamı hedef sayıya (50) ne kadar yakınsa, uygunluk değeri o kadar yüksek olacaktır. Uygunluk fonksiyonu şu şekilde ifade edilir:
    fitness = |sum(individual) - target_sum|
  Burada, `individual`, bireyin genetik dizisini temsil eder.

- Mutasyon Fonksiyonu: Bireylerde rastgele değişiklikler yapar. Bu örnekte, herhangi bir genin rastgele bir gen pool elemanı ile değiştirilme olasılığı vardır. Mutasyon fonksiyonu şu şekilde ifade edilir:
    P(gen değişimi) = 0.1
  Burada, `gen değişimi`, rastgele seçilen bir genin değiştirilme olasılığını temsil eder.

Kullanım:
1. Python yüklü olduğundan emin olun.
2. Terminal veya komut istemcisinde proje dizinine gidin.
3. Ana dizindeki `main.py` dosyasını çalıştırın.
4. Çıktıyı gözlemleyin ve çözümü inceleyin.

Not: Bu proje, genetik algoritmaların temel prensiplerini anlamak ve basit bir problemin nasıl çözülebileceğini göstermek için tasarlanmıştır. Gerçek dünya problemleri için daha karmaşık ve özelleştirilmiş çözümler gerekebilir.
