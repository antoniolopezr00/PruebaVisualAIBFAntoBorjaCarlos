from django.urls import path
from jiade import jiade_views
app_name='jiade'
urlpatterns = [


    


    path('',jiade_views.index,name="index"),
    path('index/',jiade_views.index,name="index"),
    path('index-2/',jiade_views.index_2,name="index-2"),
    path('market/',jiade_views.market,name="market"),
    path('coin-details/',jiade_views.coin_details,name="coin-details"),
    path('portfolio/',jiade_views.portfolio,name="portfolio"),

    path('ico-listing/',jiade_views.ico_listing,name="ico-listing"),
    path('p2p/',jiade_views.p2p,name="p2p"),
    path('future/',jiade_views.future,name="future"),
    path('trading-market/',jiade_views.trading_market,name="trading-market"),

    path('market-watch/',jiade_views.market_watch,name="market-watch"),
    path('exchange/',jiade_views.exchange,name="exchange"),
    path('banking/',jiade_views.banking,name="banking"),

    path('history/',jiade_views.history,name="history"),
    path('orders/',jiade_views.orders,name="orders"),
    path('reports/',jiade_views.reports,name="reports"),
    path('user/',jiade_views.user,name="user"),

    path('app-profile/',jiade_views.app_profile,name="app-profile"),
    path('edit-profile/',jiade_views.edit_profile,name="edit-profile"),
    path('post-details/',jiade_views.post_details,name="post-details"),
    path('email-compose/',jiade_views.email_compose,name="email-compose"),
    path('email-inbox/',jiade_views.email_inbox,name="email-inbox"),
    path('email-read/',jiade_views.email_read,name="email-read"),
    path('app-calender/',jiade_views.app_calender,name="app-calender"),
    path('ecom-product-grid/',jiade_views.ecom_product_grid,name="ecom-product-grid"),
    path('ecom-product-list/',jiade_views.ecom_product_list,name="ecom-product-list"),
    path('ecom-product-detail/',jiade_views.ecom_product_detail,name="ecom-product-detail"),
    path('ecom-product-order/',jiade_views.ecom_product_order,name="ecom-product-order"),
    path('ecom-checkout/',jiade_views.ecom_checkout,name="ecom-checkout"),
    path('ecom-invoice/',jiade_views.ecom_invoice,name="ecom-invoice"),
    path('ecom-customers/',jiade_views.ecom_customers,name="ecom-customers"),
    path('chart-flot/',jiade_views.chart_flot,name="chart-flot"),
    path('chart-morris/',jiade_views.chart_morris,name="chart-morris"),
    path('chart-chartjs/',jiade_views.chart_chartjs,name="chart-chartjs"),
    path('chart-chartist/',jiade_views.chart_chartist,name="chart-chartist"),
    path('chart-sparkline/',jiade_views.chart_sparkline,name="chart-sparkline"),
    path('chart-peity/',jiade_views.chart_peity,name="chart-peity"),

    path('content/',jiade_views.content,name="content"),
    path('add-content/',jiade_views.add_content,name="add-content"),
    path('menu/',jiade_views.menu,name="menu"),
    path('email-template/',jiade_views.email_template,name="email-template"),
    path('add-email/',jiade_views.add_email,name="add-email"),
    path('blog/',jiade_views.blog,name="blog"),
    path('add-blog/',jiade_views.add_blog,name="add-blog"),
    path('blog-category/',jiade_views.blog_category,name="blog-category"),

    path('ui-accordion/',jiade_views.ui_accordion,name="ui-accordion"),
    path('ui-alert/',jiade_views.ui_alert,name="ui-alert"),
    path('ui-badge/',jiade_views.ui_badge,name="ui-badge"),
    path('ui-button/',jiade_views.ui_button,name="ui-button"),
    path('ui-modal/',jiade_views.ui_modal,name="ui-modal"),
    path('ui-button-group/',jiade_views.ui_button_group,name="ui-button-group"),
    path('ui-list-group/',jiade_views.ui_list_group,name="ui-list-group"),
    path('ui-card/',jiade_views.ui_card,name="ui-card"),
    path('ui-carousel/',jiade_views.ui_carousel,name="ui-carousel"),
    path('ui-dropdown/',jiade_views.ui_dropdown,name="ui-dropdown"),
    path('ui-popover/',jiade_views.ui_popover,name="ui-popover"),
    path('ui-progressbar/',jiade_views.ui_progressbar,name="ui-progressbar"),
    path('ui-tab/',jiade_views.ui_tab,name="ui-tab"),
    path('ui-typography/',jiade_views.ui_typography,name="ui-typography"),
    path('ui-pagination/',jiade_views.ui_pagination,name="ui-pagination"),
    path('ui-grid/',jiade_views.ui_grid,name="ui-grid"),
    

    path('uc-select2/',jiade_views.uc_select2,name="uc-select2"),
    path('uc-nestable/',jiade_views.uc_nestable,name="uc-nestable"),
    path('uc-noui-slider/',jiade_views.uc_noui_slider,name="uc-noui-slider"),
    path('uc-sweetalert/',jiade_views.uc_sweetalert,name="uc-sweetalert"),
    path('uc-toastr/',jiade_views.uc_toastr,name="uc-toastr"),
    path('map-jqvmap/',jiade_views.map_jqvmap,name="map-jqvmap"),
    path('uc-lightgallery/',jiade_views.uc_lightgallery,name="uc-lightgallery"),

    path('widget-basic/',jiade_views.widget_basic,name="widget-basic"),

    path('form-element/',jiade_views.form_element,name="form-element"),
    path('form-wizard/',jiade_views.form_wizard,name="form-wizard"),
    path('form-editor/',jiade_views.form_editor,name="form-editor"),
    path('form-pickers/',jiade_views.form_pickers,name="form-pickers"),
    path('form-validation/',jiade_views.form_validation,name="form-validation"),

    path('table-bootstrap-basic/',jiade_views.table_bootstrap_basic,name="table-bootstrap-basic"),
    path('table-datatable-basic/',jiade_views.table_datatable_basic,name="table-datatable-basic"),


    path('page-login/',jiade_views.page_login,name="page-login"),
    path('page-register/',jiade_views.page_register,name="page-register"),
    path('page-forgot-password/',jiade_views.page_forgot_password,name="page-forgot-password"),
    path('page-lock-screen/',jiade_views.page_lock_screen,name="page-lock-screen"),
    path('page-empty/',jiade_views.page_empty,name="page-empty"),
    path('page-error-400/',jiade_views.page_error_400,name="page-error-400"),
    path('page-error-403/',jiade_views.page_error_403,name="page-error-403"),
    path('page-error-404/',jiade_views.page_error_404,name="page-error-404"),
    path('page-error-500/',jiade_views.page_error_500,name="page-error-500"),
    path('page-error-503/',jiade_views.page_error_503,name="page-error-503"),
    
    #Nuevos de antonio
    path('trend/',jiade_views.trend, name="trend"),
    path('seasonal/',jiade_views.seasonal, name="seasonal"),
    path('sarimax_arima/',jiade_views.sarimax_arima, name="sarimax_arima"),
    path('residuos/',jiade_views.residuos, name="residuos"),
    path('prueba_adf/',jiade_views.prueba_adf, name="prueba_adf"),
    path('prevision/',jiade_views.prevision, name="prevision"),
    path('autocorrelacion/',jiade_views.autocorrelacion, name="autocorrelacion"),
    path('random_forest/',jiade_views.random_forest, name="random_forest"),
    path('matriz_confusion/',jiade_views.matriz_confusion, name="matriz_confusion"),
    path('lead_source/',jiade_views.lead_source, name="lead_source"),
    path('last_activity/',jiade_views.last_activity, name="last_activity"),
    path('histograma/',jiade_views.histograma, name="histograma"),
    path('grafico_caja/',jiade_views.grafico_caja, name="grafico_caja"),
    path('distribucion_lead/',jiade_views.distribucion_lead, name="distribucion_lead"),
    path('curva_rac/',jiade_views.curva_rac, name="curva_rac"),
    path('count/',jiade_views.count, name="count"),
    path('costos_beneficos/',jiade_views.costos_beneficios, name="costos_beneficos"),
    path('arboles_decision/',jiade_views.arboles_decision, name="arboles_decision"),

]