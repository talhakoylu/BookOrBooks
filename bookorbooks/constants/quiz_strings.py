class QuizStrings():
    class AbstractBaseStrings():
        created_at_verbose_name = "Oluşturulma Tarihi"
        updated_at_verbose_name = "Güncellenme Tarihi"

    class QuizStrings():
        book_verbose_name = "Kitap"
        title_verbose_name = "Başlık"
        enabled_verbose_name = "Sınav Aktif Mi?"
        meta_quiz_verbose_name = "Sınav"
        meta_quiz_verbose_name_plural = "Sınavlar"

    class QuestionStrings():
        quiz_verbose_name = "Sınav"
        question_verbose_name = "Soru"
        topic_verbose_name = "Konu"
        topic_hint_text = "Rapor sayfasında, cevabın yanlış olması durumunda gösterilecek metin."
        meta_question_verbose_name = "Soru"
        meta_question_verbose_name_plural = "Sorular"

    class AnswerStrings():
        answer_verbose_name = "Cevap"
        question_verbose_name = "Soru"
        is_correct_verbose_name = "Doğru Bir Cevap Mı?"
        meta_answer_verbose_name = "Cevap"
        meta_answer_verbose_name_plural = "Cevaplar"

    class TakingQuizStrings():
        quiz_verbose_name = "Sınav"
        child_verbose_name = "Çocuk"
        title_verbose_name = "Başlık"
        total_point_verbose_name = "Toplam Puan"
        meta_verbose_name = "Çözülmüş Sınav Kaydı" 
        meta_verbose_name_plural = "Çözülmüş Sınav Kayıtları" 
    
    class TakingQuizAnswersStrings():
        taking_quiz_verbose_name = "Girilen Sınav"
        taking_quiz_title_verbose_name = "Girilen Sınav Başlığı"
        question_verbose_name = "Soru"
        question_topic_verbose_name = "Sorunun Konusu"
        answer_verbose_name = "Cevap"
        answer_is_correct_verbose_name = "Cevap Doğru Mu?"
        total_point_verbose_name = "Toplam Puan"
        meta_verbose_name = "Çözülmüş Sınav Cevabı" 
        meta_verbose_name_plural = "Çözülmüş Sınav Cevapları" 

    class ValidationErrorMessages():
        answer_is_not_belong_to_quiz = "This answer does not belong to the question you chose, please check it."
        question_is_not_belong_to_quiz = "This question does not belong to the exam you chose, please check it."