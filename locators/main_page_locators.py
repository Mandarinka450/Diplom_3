from selenium.webdriver.common.by import By


class MainPageLocators:
    LINK_CONSTRUCTOR = (By.XPATH, './/p[contains(text(), "Конструктор")]/parent::a')  # ссылка на переход в раздел "Конструктор"
    LINK_RIBBON_ORDERS = (By.XPATH, './/p[contains(text(), "Лента Заказов")]/parent::a') # ссылка на раздел "Лента заказов"
    TITLE_RIBBON_ORDERS = (By.XPATH, './/h1[contains(text(), "Лента заказов")]')  # заголовок ленты заказов
    CARD_ROLL = (By.XPATH, './/ul[@class="BurgerIngredients_ingredients__list__2A-mT"]/*') # карточка с булочкой
    SECTION_MODAL_WINDOW = (By.XPATH, './/div[@class="Modal_modal__container__Wo2l_"]/parent::section') # модальное окно
    CLOSE_MODAL_WINDOW = (By.XPATH, './/div[@class="Modal_modal__container__Wo2l_"]/child::button') # кнопка закрытия модального окна
    CARD_ORDER = (By.XPATH, './/li[@class="OrderHistory_listItem__2x95r mb-6"]/child::a') # карточка заказа в списке
    SECTION_MODAL_WINDOW_ORDER = (By.XPATH, './/section[2]')  # модальное окно заказа
    DESTINATION = (By.XPATH, './/ul[@class="BurgerConstructor_basket__list__l9dp_"]') # блок, куда необходимо перетащить ингредиент
    COUNTER = (By.XPATH, './/p[@class="counter_counter__num__3nue1"]')  # каунтер
    BUTTON_CREATE_ORDER = (By.XPATH, './/button[contains(text(), "Оформить заказ")]')  # кнопка "Оформить заказ"
    TEXT_CREATE_ORDER = (By.XPATH, './/p[@class="undefined text text_type_main-small mb-2"]')  # текст успешного оформленного заказа
    ID_ORDER = (By.XPATH, './/p[contains(text(), "идентификатор заказа")]')
    LI_NUMBER_ORDERS = (By.XPATH, './/li[@class="text text_type_digits-default mb-2"]')
    NUMBER_ORDER = (By.XPATH, './/div[@class="Modal_modal__contentBox__sCy8X pt-30 pb-30"]/h2')

