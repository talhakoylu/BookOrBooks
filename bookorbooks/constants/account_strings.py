class AccountStrings():
    class CustomUserStrings():
        gender_choice_male = "Erkek"
        gender_choice_female = "Kadın"
        gender_choice_other = "Other"
        user_type_choice_child = "Çocuk"
        user_type_choice_parent = "Ebeveyn"
        user_type_choice_instructor = "Eğitmen"
        user_type_choice_default = "Default"
        user_type_choice_admin = "Yönetici"
        identity_number_verbose_name = "Kimlik Numarası"
        birth_date_verbose_name = "Doğum Tarihi"
        gender_verbose_name = "Cinsiyet"
        user_type_verbose_name = "Hesap Türü"
        meta_verbose_name = "Kullanıcı"
        meta_verbose_name_plural = "Kullanıcılar"

    class ChildProfileStrings():
        user_verbose_name = "Kullanıcı"
        city_verbose_name = "Şehir"
        hobbies_verbose_name = "Hobiler"
        meta_verbose_name = "Çocuk"
        meta_verbose_name_plural = "Çocuklar"
        user_type_error = "Kullanıcı bir çocuk olarak belirtilmemiş, ekleyebilmek için önce hesap ayarlarından statüsünü çocuk yapın!"
    
    class ParentProfileStrings():
        user_verbose_name = "Kullanıcı"
        city_verbose_name = "Şehir"
        profession_verbose_name = "Meslek"
        meta_verbose_name = "Ebeveyn"
        meta_verbose_name_plural = "Ebeveynler"
        user_type_error = "Kullanıcı bir ebevyn olarak belirtilmemiş, ekleyebilmek için önce hesap ayarlarından statüsünü ebeveyn yapın!"

    class ChildListString():
        parent_verbose_name = "Ebeveyn"
        child_verbose_name = "Çocuk"
        meta_verbose_name = "Ebeveyn ve Çocuk Kaydı"
        meta_verbose_name_plural = "Ebeveyn ve Çocuk Kayıtları"

    class RegisterSerializerStrings():
        user_type_error = "You cannot pass data other than: 1- default, 2- child, 3- parent, 4- instructor"
        gender_error = "You cannot pass data other than: 1- male, 2- female, 3- other"
        identity_number_error = "Identity number can only consist of numbers and cannot be long than 11."

    class PermissionStrings():
        is_parent_message = "To do this, you must be a parent."