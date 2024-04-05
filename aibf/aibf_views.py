from django.shortcuts import render




    

def index(request):
    context={
        "page_title":"Dashboard"
    }
    return render(request,'aibf/index.html',context)


def index_2(request):
    context={
        "page_title":"Dashboard Dark"
    }
    return render(request,'aibf/index-2.html',context)


def market(request):
    context={
        "page_title":"Market"
    }
    return render(request,'aibf/market.html',context)


def coin_details(request):
    context={
        "page_title":"Coin Details"
    }
    return render(request,'aibf/coin-details.html',context)


def portfolio(request):
    context={
        "page_title":"Portfolio"
    }
    return render(request,'aibf/portfolio.html',context)


def ico_listing(request):
    context={
        "page_title":"ICO Listing"
    }
    return render(request,'aibf/trading/ico-listing.html',context)


def p2p(request):
    context={
        "page_title":"P2P"
    }
    return render(request,'aibf/trading/p2p.html',context)


def future(request):
    context={
        "page_title":"Future Trading"
    }
    return render(request,'aibf/trading/future.html',context)


def trading_market(request):
    context={
        "page_title":"Trading Market"
    }
    return render(request,'aibf/trading/trading-market.html',context)


def market_watch(request):
    context={
        "page_title":"Market Watch"
    }
    return render(request,'aibf/crypto/market-watch.html',context)


def exchange(request):
    context={
        "page_title":"Exchange"
    }
    return render(request,'aibf/crypto/exchange.html',context)


def banking(request):
    context={
        "page_title":"Banking"
    }
    return render(request,'aibf/crypto/banking.html',context)


def history(request):
    context={
        "page_title":"History"
    }
    return render(request,'aibf/reports/history.html',context)


def orders(request):
    context={
        "page_title":"Orders"
    }
    return render(request,'aibf/reports/orders.html',context) 	


def reports(request):
    context={
        "page_title":"Reports"
    }
    return render(request,'aibf/reports/report.html',context)


def user(request):
    context={
        "page_title":"User"
    }
    return render(request,'aibf/reports/user.html',context)


def content(request):
    context={
        "page_title":"Content"
    }
    return render(request,'aibf/cms/content.html',context)


def add_content(request):
    context={
        "page_title":"Add Content"
    }
    return render(request,'aibf/cms/add-content.html',context)


def menu(request):
    context={
        "page_title":"Menu"
    }
    return render(request,'aibf/cms/menu.html',context)


def perfil_template(request):
    context={
        "page_title":"perfil Template"
    }
    return render(request,'aibf/cms/perfil-template.html',context)


def add_perfil(request):
    context={
        "page_title":"Add perfil"
    }
    return render(request,'aibf/cms/add-perfil.html',context)


def blog(request):
    context={
        "page_title":"Blog"
    }
    return render(request,'aibf/cms/blog.html',context)


def add_blog(request):
    context={
        "page_title":"Add Blog"
    }
    return render(request,'aibf/cms/add-blog.html',context)


def blog_category(request):
    context={
        "page_title":"Blog Category"
    }
    return render(request,'aibf/cms/blog-category.html',context)


def app_profile(request):
    context={
        "page_title":"App Profile"
    }
    return render(request,'aibf/apps/mi_perfil.html',context)


def edit_profile(request):
    context={
        "page_title":"Edit Profile"
    }
    return render(request,'aibf/apps/edit-profile.html',context)


def post_details(request):
    context={
        "page_title":"Post Details"
    }
    return render(request,'aibf/apps/post-details.html',context)


def perfil_compose(request):
    context={
        "page_title":"Compose"
    }
    return render(request,'aibf/apps/perfil/perfil-compose.html',context)


def perfil_inbox(request):
    context={
        "page_title":"Inbox"
    }
    return render(request,'aibf/apps/perfil/perfil-inbox.html',context)


def perfil_read(request):
    context={
        "page_title":"Read"
    }
    return render(request,'aibf/apps/perfil/perfil-read.html',context)


def app_calender(request):
    context={
        "page_title":"Calendar"
    }
    return render(request,'aibf/apps/app-calender.html',context)


def ecom_product_grid(request):
    context={
        "page_title":"Product Grid"
    }
    return render(request,'aibf/apps/shop/ecom-product-grid.html',context)


def ecom_product_list(request):
    context={
        "page_title":"Product List"
    }
    return render(request,'aibf/apps/shop/ecom-product-list.html',context)


def ecom_product_detail(request):
    context={
        "page_title":"Product Detail"
    }
    return render(request,'aibf/apps/shop/ecom-product-detail.html',context)


def ecom_product_order(request):
    context={
        "page_title":"Product Order"
    }
    return render(request,'aibf/apps/shop/ecom-product-order.html',context)


def ecom_checkout(request):
    context={
        "page_title":"Checkout"
    }
    return render(request,'aibf/apps/shop/ecom-checkout.html',context)


def ecom_invoice(request):
    context={
        "page_title":"Invoice"
    }
    return render(request,'aibf/apps/shop/ecom-invoice.html',context)


def ecom_customers(request):
    context={
        "page_title":"Customers"
    }
    return render(request,'aibf/apps/shop/ecom-customers.html',context)



def chart_flot(request):
    context={
        "page_title":"Chart Flot"
    }
    return render(request,'aibf/charts/chart-flot.html',context)


def chart_morris(request):
    context={
        "page_title":"Chart Morris"
    }
    return render(request,'aibf/charts/chart-morris.html',context)


def chart_chartjs(request):
    context={
        "page_title":"Chart Chartjs"
    }
    return render(request,'aibf/charts/chart-chartjs.html',context)


def chart_chartist(request):
    context={
        "page_title":"Chart Chartist"
    }
    return render(request,'aibf/charts/chart-chartist.html',context)


def chart_sparkline(request):
    context={
        "page_title":"Chart Sparkline"
    }
    return render(request,'aibf/charts/chart-sparkline.html',context)


def chart_peity(request):
    context={
        "page_title":"Chart Peity"
    }
    return render(request,'aibf/charts/chart-peity.html',context)



def ui_accordion(request):
    context={
        "page_title":"Accordion"
    }
    return render(request,'aibf/bootstrap/ui-accordion.html',context)


def ui_alert(request):
    context={
        "page_title":"Alert"
    }
    return render(request,'aibf/bootstrap/ui-alert.html',context)


def ui_badge(request):
    context={
        "page_title":"Badge"
    }
    return render(request,'aibf/bootstrap/ui-badge.html',context)


def ui_button(request):
    context={
        "page_title":"Button"
    }
    return render(request,'aibf/bootstrap/ui-button.html',context)


def ui_modal(request):
    context={
        "page_title":"Modal"
    }
    return render(request,'aibf/bootstrap/ui-modal.html',context)


def ui_button_group(request):
    context={
        "page_title":"Button Group"
    }
    return render(request,'aibf/bootstrap/ui-button-group.html',context)


def ui_list_group(request):
    context={
        "page_title":"List Group"
    }
    return render(request,'aibf/bootstrap/ui-list-group.html',context)


def ui_card(request):
    context={
        "page_title":"Card"
    }
    return render(request,'aibf/bootstrap/ui-card.html',context)


def ui_carousel(request):
    context={
        "page_title":"Carousel"
    }
    return render(request,'aibf/bootstrap/ui-carousel.html',context)


def ui_dropdown(request):
    context={
        "page_title":"Dropdown"
    }
    return render(request,'aibf/bootstrap/ui-dropdown.html',context)


def ui_popover(request):
    context={
        "page_title":"Popover"
    }
    return render(request,'aibf/bootstrap/ui-popover.html',context)


def ui_progressbar(request):
    context={
        "page_title":"Progressbar"
    }
    return render(request,'aibf/bootstrap/ui-progressbar.html',context)


def ui_tab(request):
    context={
        "page_title":"Tab"
    }
    return render(request,'aibf/bootstrap/ui-tab.html',context)


def ui_typography(request):
    context={
        "page_title":"Typography"
    }
    return render(request,'aibf/bootstrap/ui-typography.html',context)


def ui_pagination(request):
    context={
        "page_title":"Pagination"
    }
    return render(request,'aibf/bootstrap/ui-pagination.html',context)


def ui_grid(request):
    context={
        "page_title":"Grid"
    }
    return render(request,'aibf/bootstrap/ui-grid.html',context)


def uc_select2(request):
    context={
        "page_title":"Select"
    }
    return render(request,'aibf/plugins/uc-select2.html',context)


def uc_nestable(request):
    context={
        "page_title":"Nestable"
    }
    return render(request,'aibf/plugins/uc-nestable.html',context)


def uc_noui_slider(request):
    context={
        "page_title":"UI Slider"
    }
    return render(request,'aibf/plugins/uc-noui-slider.html',context)


def uc_sweetalert(request):
    context={
        "page_title":"Sweet Alert"
    }
    return render(request,'aibf/plugins/uc-sweetalert.html',context)


def uc_toastr(request):
    context={
        "page_title":"Toastr"
    }
    return render(request,'aibf/plugins/uc-toastr.html',context)


def map_jqvmap(request):
    context={
        "page_title":"Jqvmap"
    }
    return render(request,'aibf/plugins/map-jqvmap.html',context)


def uc_lightgallery(request):
    context={
        "page_title":"LightGallery"
    }
    return render(request,'aibf/plugins/uc-lightgallery.html',context)


def widget_basic(request):
    context={
        "page_title":"Widget"
    }
    return render(request,'aibf/widget-basic.html',context)

def form_element(request):
    context={
        "page_title":"Form Element"
    }
    return render(request,'aibf/forms/form-element.html',context)


def form_wizard(request):
    context={
        "page_title":"Form Wizard"
    }
    return render(request,'aibf/forms/form-wizard.html',context)


def form_editor(request):
    context={
        "page_title":"CkEditor"
    }
    return render(request,'aibf/forms/form-editor.html',context)


def form_pickers(request):
    context={
        "page_title":"Pickers"
    }
    return render(request,'aibf/forms/form-pickers.html',context)


def form_validation(request):
    context={
        "page_title":"Form Validation"
    }
    return render(request,'aibf/forms/form-validation.html',context)


def table_bootstrap_basic(request):
    context={
        "page_title":"Table Bootstrap"
    }
    return render(request,'aibf/table/table-bootstrap-basic.html',context)


def table_datatable_basic(request):
    context={
        "page_title":"Table Datatable"
    }
    return render(request,'aibf/table/table-datatable-basic.html',context)




def page_register(request):
    return render(request,'aibf/pages/page-register.html')

def page_login(request):
    return render(request,'aibf/pages/page-login.html')

def page_forgot_password(request):
    return render(request,'aibf/pages/page-forgot-password.html')

def page_lock_screen(request):
    return render(request,'aibf/pages/page-lock-screen.html')

def page_empty(request):
    context={
        "page_title":"Empty Page"
    }
    return render(request,'aibf/pages/page-empty.html',context)

def page_error_400(request):
    return render(request,'400.html')
    
def page_error_403(request):
    return render(request,'403.html')

def page_error_404(request):
    return render(request,'404.html')

def page_error_500(request):
    return render(request,'500.html')

def page_error_503(request):
    return render(request,'503.html')

#Nuevos de Antonio

def trend(request):
    return render(request,'aibf/usuario/series_tiempo/trend.html')

def seasonal(request):
    return render(request,'aibf/usuario/series_tiempo/seasonal.html')


def sarimax_arima(request):
    return render(request,'aibf/usuario/series_tiempo/sarimax_arima.html')

def residuos(request):
    return render(request,'aibf/usuario/series_tiempo/residuos.html')

def prueba_adf(request):
    return render(request,'aibf/usuario/series_tiempo/prueba_adf.html')

def prevision(request):
    return render(request,'aibf/usuario/series_tiempo/prevision.html')

def autocorrelacion(request):
    return render(request,'aibf/usuario/series_tiempo/autocorrelacion.html')

def random_forest(request):
    return render(request,'aibf/usuario/random_forest/random_forest.html')

def arboles_decision(request):
    return render(request,'aibf/usuario/arboles_decision/arboles_decision.html')

def costos_beneficios(request):
    return render(request,'aibf/usuario/autocorrelacion/costos_beneficios.html')

def count(request):
    return render(request,'aibf/usuario/autocorrelacion/count.html')

def curva_roc(request):
    return render(request,'aibf/usuario/autocorrelacion/curva_roc.html')

def distribucion_lead(request):
    return render(request,'aibf/usuario/autocorrelacion/distribucion_lead.html')

def grafico_caja(request):
    return render(request,'aibf/usuario/autocorrelacion/grafico_caja.html')

def histograma(request):
    return render(request,'aibf/usuario/autocorrelacion/histograma.html')

def last_activity(request):
    return render(request,'aibf/usuario/autocorrelacion/last_activity.html')

def lead_source(request):
    return render(request,'aibf/usuario/autocorrelacion/lead_source.html')

def matriz_confusion(request):
    return render(request,'aibf/usuario/autocorrelacion/matriz_confusion.html')


















