from django.urls import path
from aibf import aibf_views
from django.contrib import admin
from django.urls import path, include
from analytic_app.views import reporte, envio_datos, envio_json, time_series

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recibir/', reporte, name='home'),  # Esto manejará la URL raíz,
    path('enviar/', envio_datos, name='envio'), 
    path('enviar2/', envio_json, name='envioJson'),  
    path("time_series/", time_series, name = 'series_tiempo'),
]



app_name='aibf'
urlpatterns = [


    


    path('',aibf_views.index,name="index"),
    path('index/',aibf_views.index,name="index"),
    path('index-2/',aibf_views.index_2,name="index-2"),
    path('market/',aibf_views.market,name="market"),
    path('coin-details/',aibf_views.coin_details,name="coin-details"),
    path('portfolio/',aibf_views.portfolio,name="portfolio"),

    path('ico-listing/',aibf_views.ico_listing,name="ico-listing"),
    path('p2p/',aibf_views.p2p,name="p2p"),
    path('future/',aibf_views.future,name="future"),
    path('trading-market/',aibf_views.trading_market,name="trading-market"),

    path('market-watch/',aibf_views.market_watch,name="market-watch"),
    path('exchange/',aibf_views.exchange,name="exchange"),
    path('banking/',aibf_views.banking,name="banking"),

    path('history/',aibf_views.history,name="history"),
    path('orders/',aibf_views.orders,name="orders"),
    path('reports/',aibf_views.reports,name="reports"),
    path('user/',aibf_views.user,name="user"),

    path('mi_perfil/',aibf_views.app_profile,name="mi_perfil"),
    path('edit-profile/',aibf_views.edit_profile,name="edit-profile"),
    path('post-details/',aibf_views.post_details,name="post-details"),
    path('perfil-compose/',aibf_views.perfil_compose,name="perfil-compose"),
    path('perfil-inbox/',aibf_views.perfil_inbox,name="perfil-inbox"),
    path('perfil-read/',aibf_views.perfil_read,name="perfil-read"),
    path('app-calender/',aibf_views.app_calender,name="app-calender"),
    path('ecom-product-grid/',aibf_views.ecom_product_grid,name="ecom-product-grid"),
    path('ecom-product-list/',aibf_views.ecom_product_list,name="ecom-product-list"),
    path('ecom-product-detail/',aibf_views.ecom_product_detail,name="ecom-product-detail"),
    path('ecom-product-order/',aibf_views.ecom_product_order,name="ecom-product-order"),
    path('ecom-checkout/',aibf_views.ecom_checkout,name="ecom-checkout"),
    path('ecom-invoice/',aibf_views.ecom_invoice,name="ecom-invoice"),
    path('ecom-customers/',aibf_views.ecom_customers,name="ecom-customers"),
    path('chart-flot/',aibf_views.chart_flot,name="chart-flot"),
    path('chart-morris/',aibf_views.chart_morris,name="chart-morris"),
    path('chart-chartjs/',aibf_views.chart_chartjs,name="chart-chartjs"),
    path('chart-chartist/',aibf_views.chart_chartist,name="chart-chartist"),
    path('chart-sparkline/',aibf_views.chart_sparkline,name="chart-sparkline"),
    path('chart-peity/',aibf_views.chart_peity,name="chart-peity"),

    path('content/',aibf_views.content,name="content"),
    path('add-content/',aibf_views.add_content,name="add-content"),
    path('menu/',aibf_views.menu,name="menu"),
    path('perfil-template/',aibf_views.perfil_template,name="perfil-template"),
    path('add-perfil/',aibf_views.add_perfil,name="add-perfil"),
    path('blog/',aibf_views.blog,name="blog"),
    path('add-blog/',aibf_views.add_blog,name="add-blog"),
    path('blog-category/',aibf_views.blog_category,name="blog-category"),

    path('ui-accordion/',aibf_views.ui_accordion,name="ui-accordion"),
    path('ui-alert/',aibf_views.ui_alert,name="ui-alert"),
    path('ui-badge/',aibf_views.ui_badge,name="ui-badge"),
    path('ui-button/',aibf_views.ui_button,name="ui-button"),
    path('ui-modal/',aibf_views.ui_modal,name="ui-modal"),
    path('ui-button-group/',aibf_views.ui_button_group,name="ui-button-group"),
    path('ui-list-group/',aibf_views.ui_list_group,name="ui-list-group"),
    path('ui-card/',aibf_views.ui_card,name="ui-card"),
    path('ui-carousel/',aibf_views.ui_carousel,name="ui-carousel"),
    path('ui-dropdown/',aibf_views.ui_dropdown,name="ui-dropdown"),
    path('ui-popover/',aibf_views.ui_popover,name="ui-popover"),
    path('ui-progressbar/',aibf_views.ui_progressbar,name="ui-progressbar"),
    path('ui-tab/',aibf_views.ui_tab,name="ui-tab"),
    path('ui-typography/',aibf_views.ui_typography,name="ui-typography"),
    path('ui-pagination/',aibf_views.ui_pagination,name="ui-pagination"),
    path('ui-grid/',aibf_views.ui_grid,name="ui-grid"),
    

    path('uc-select2/',aibf_views.uc_select2,name="uc-select2"),
    path('uc-nestable/',aibf_views.uc_nestable,name="uc-nestable"),
    path('uc-noui-slider/',aibf_views.uc_noui_slider,name="uc-noui-slider"),
    path('uc-sweetalert/',aibf_views.uc_sweetalert,name="uc-sweetalert"),
    path('uc-toastr/',aibf_views.uc_toastr,name="uc-toastr"),
    path('map-jqvmap/',aibf_views.map_jqvmap,name="map-jqvmap"),
    path('uc-lightgallery/',aibf_views.uc_lightgallery,name="uc-lightgallery"),

    path('widget-basic/',aibf_views.widget_basic,name="widget-basic"),

    path('form-element/',aibf_views.form_element,name="form-element"),
    path('form-wizard/',aibf_views.form_wizard,name="form-wizard"),
    path('form-editor/',aibf_views.form_editor,name="form-editor"),
    path('form-pickers/',aibf_views.form_pickers,name="form-pickers"),
    path('form-validation/',aibf_views.form_validation,name="form-validation"),

    path('table-bootstrap-basic/',aibf_views.table_bootstrap_basic,name="table-bootstrap-basic"),
    path('table-datatable-basic/',aibf_views.table_datatable_basic,name="table-datatable-basic"),


    path('page-login/',aibf_views.page_login,name="page-login"),
    path('page-register/',aibf_views.page_register,name="page-register"),
    path('page-forgot-password/',aibf_views.page_forgot_password,name="page-forgot-password"),
    path('page-lock-screen/',aibf_views.page_lock_screen,name="page-lock-screen"),
    path('page-empty/',aibf_views.page_empty,name="page-empty"),
    path('page-error-400/',aibf_views.page_error_400,name="page-error-400"),
    path('page-error-403/',aibf_views.page_error_403,name="page-error-403"),
    path('page-error-404/',aibf_views.page_error_404,name="page-error-404"),
    path('page-error-500/',aibf_views.page_error_500,name="page-error-500"),
    path('page-error-503/',aibf_views.page_error_503,name="page-error-503"),
    
    #Nuevos de antonio
    path('trend/',aibf_views.trend, name="trend"),
    path('seasonal/',aibf_views.seasonal, name="seasonal"),
    path('sarimax_arima/',aibf_views.sarimax_arima, name="sarimax_arima"),
    path('residuos/',aibf_views.residuos, name="residuos"),
    path('prueba_adf/',aibf_views.prueba_adf, name="prueba_adf"),
    path('prevision/',aibf_views.prevision, name="prevision"),
    path('autocorrelacion/',aibf_views.autocorrelacion, name="autocorrelacion"),
    path('random_forest/',aibf_views.random_forest, name="random_forest"),
    path('matriz_confusion/',aibf_views.matriz_confusion, name="matriz_confusion"),
    path('lead_source/',aibf_views.lead_source, name="lead_source"),
    path('last_activity/',aibf_views.last_activity, name="last_activity"),
    path('histograma/',aibf_views.histograma, name="histograma"),
    path('grafico_caja/',aibf_views.grafico_caja, name="grafico_caja"),
    path('distribucion_lead/',aibf_views.distribucion_lead, name="distribucion_lead"),
    path('curva_roc/',aibf_views.curva_roc, name="curva_roc"),
    path('count/',aibf_views.count, name="count"),
    path('costos_beneficios/',aibf_views.costos_beneficios,name="costos_beneficios"),
    path('arboles_decision/',aibf_views.arboles_decision, name="arboles_decision"),
 
    
]

    