class BookStrings():
    class BookLanguageStrings():
        meta_verbose_name = "Dil"
        meta_verbose_name_plural = "Diller"
        language_name_verbose_name = "Dil"
        language_code_verbose_name = "Dil Kodu"

    class AbstractBaseModelStrings():
        created_at_verbose_name = "Oluşturulma Tarihi"
        updated_at_verbose_name = "Güncellenme Tarihi"

    class CategoryStrings():
        title_verbose_name = "Başlık"
        description_verbose_name = "Açıklama"
        meta_verbose_name = "Kategori"
        meta_verbose_name_plural = "Kategoriler"

    class BookLevelStrings():
        title_verbose_name = "Başlık"
        meta_verbose_name = "Seviye"
        meta_verbose_name_plural = "Kitap Seviyeleri"

    class BookStrings():
        category_verbose_name = "Kategori"
        level_verbose_name = "Seviye"
        language_verbose_name = "Kitap Dili"
        name_verbose_name = "İsim"
        description_verbose_name = "Açıklama"
        author_verbose_name = "Yazar"
        page_verbose_name = "Sayfa Sayısı"
        cover_image_verbose_name = "Kapak Görseli"
        meta_verbose_name = "Kitap"
        meta_verbose_name_plural = "Kitaplar"

    class Author():
        first_name_verbose_name = "İsim"
        last_name_verbose_name = "Soyisim"
        photo_verbose_name = "Fotoğraf"
        biography_verbose_name = "Biyografi"
        meta_verbose_name = "Yazar"
        meta_verbose_name_plural = "Yazarlar"

    class BookPageStrings():
        book_verbose_name = "Kitap"
        title_verbose_name = "Sayfa Başlığı"
        content_verbose_name = "Sayfa İçeriği"
        page_number_verbose_name = "Sayfa Numarası"
        image_verbose_name = "Görsel"
        image_position_verbose_name = "Görselin Konumu"
        content_position_verbose_name = "İçeriğin Konumu"
        image_position_verbose_name = "Görselin Konumu"
        image_position_help_text = "0, 1, 2 değerlerine izin verilmektedir. 0 değeri en üst 2 değeri ise en altı işaret eder.\
             İçerik Konumu'yla aynı olması durumunda görsel en arkaya gönderilir ve yazı görselin üzerine gelir. Boş bırakılırsa eğer\
                 sırasıyla ilk başta görsel eklenir ve altına da yazı alanı gelir."
        meta_verbose_name = "Kitap Sayfası"
        meta_verbose_name_plural = "Kitap Sayfaları"
