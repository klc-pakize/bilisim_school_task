<h1>Bilişim School Problem API</h1>

<h3>Proje Tanımı</h3>
<p>Proje, kullanıcıların çeşitli problemlerini tanımlayan ve bu problemleri çözmek için girdi ve beklenen çıktı sağlayan bir REST API oluşturur. Her problem,  title, problem, point, level, language, input ve expected_output içerir.</p>

<h4>Bileşenler</h4>
<p>models.py dosyası, projenin veri modelini tanımlar. Aşağıdaki veri modeli kullanılır:</p>
<p>Problem: Sorunları temsil eden bir model. Bu model, title, problem, point, level, language, input ve expected_output alanlarına sahiptir.</p>

<p>serializers.py dosyası, Django Rest Framework (DRF) kullanarak veri modelini API'ye uygun JSON formatına dönüştürmek için kullanılan serializer'ları içerir. Bu proje için ProblemSerializer kullanılır.</p>

<p>signals.py dosyası, Django sinyallerini kullanarak problemlerin beklenen çıktılarını otomatik olarak hesaplar. Bu dosya, pre_save sinyali kullanır ve her bir problem öğesinin beklenen çıktısını hesaplar.</p>

<p>views.py dosyası, API görünümlerini tanımlar. Bu dosya, ProblemView sınıfını içerir ve RESTful API'yi işler. Yeni problemler oluşturabilir, mevcut problemler güncelleyebilir ve silebilirsiniz.</p>

<h2>Proje başlatmak için aşağıdaki adımları izleyin:</h2>

<p>$ git clone https://github.com/klc-pakize/bilisim_school_task.git</p>

<p>Proje dizininde sanal bir ortam oluşturun ve etkinleştirin:</p>
<ul>
    <li>$ python -m venv env</li>
    <li>$ env/Scripts/activate (for win OS)</li>
    <li>$ source env/bin/activate (for macOs/linux OS)</li>
</ul>

<p>Gerekli paketleri yükleyin:</p>
<ul> 
   <li>$ pip install -r requirements.txt</li>
</ul>

<p>.backend.env dosyasını .env olarak düzenleyin</p>
<p>.env dosyasına SECRET_KEY'i ekleyin</p>

<p>Veritabanını oluşturun ve uygulamayı başlatın:</p> 
<ul> 
   <li> $ python manage.py migrate</li>
   <li> $ python manage.py runserver</li>
</ul>

<p>Projenin Postman Collection’u için <a href="https://documenter.getpostman.com/view/23604502/2s9YC1WE6K">buraya tıklayınız.</a></p>
