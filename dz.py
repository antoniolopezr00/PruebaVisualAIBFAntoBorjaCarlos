#Static Folder Name
folder_name2 = "aibf" 
folder_name2="jiade"

dz_array = {
        "public":{
            "favicon":"/static/favicon.ico",
            "description":" Artificial Intelligence Banking Forest",
            "og_title":"Artificial Intelligence Banking Forest",
            "og_description":"Artificial Intelligence Banking Forest",
            "og_image":"https://jiade.dexignlab.com/django/social-image.png",
            "title":"Artificial Intelligence Banking Forest",
        },
        "global":{
            "css":[
                    f"{folder_name2}/vendor/bootstrap-select/dist/css/bootstrap-select.min.css",
					f"{folder_name2}/css/style.css",
                ],

            "js":{
                "top":[
                    f"{folder_name2}/vendor/global/global.min.js",
					f"{folder_name2}/vendor/bootstrap-select/dist/js/bootstrap-select.min.js",
                ],
                "bottom":[
                    f"{folder_name2}/js/dlabnav-init.js",
                    f"{folder_name2}/js/custom.min.js",
                ]
            },

        },
        "pagelevel":{
            "aibf":{#AppName
                "aibf_views":{
                    "css":{
                        "index": [
                            f"{folder_name2}/vendor/swiper/css/swiper-bundle.min.css",
                        ],
                        "index_2": [
						    f"{folder_name2}/vendor/swiper/css/swiper-bundle.min.css",
                        ],
                        "market": [
                            f"{folder_name2}/vendor/bootstrap-datetimepicker/css/bootstrap-datetimepicker.min.css",
                        ],
                        "coin_details": [
                            f"{folder_name2}/vendor/bootstrap-daterangepicker/daterangepicker.css",
                        ],
                        "portfolio": [
                            f"{folder_name2}/vendor/bootstrap-datepicker-master/css/bootstrap-datepicker.min.css",
                        ],
                        "ico_listing": [
                        ],
                        "p2p": [
                            f"{folder_name2}/vendor/datatables/css/jquery.dataTables.min.css",
                        ],
                        "future": [
                            f"{folder_name2}/vendor/datatables/css/jquery.dataTables.min.css",
                        ],
                        "trading_market": [
                            f"{folder_name2}/vendor/datatables/css/jquery.dataTables.min.css",
                        ],
                        "market_watch": [
                            f"{folder_name2}/vendor/swiper/css/swiper-bundle.min.css",
                        ],
                        "exchange": [	
                        ],
                        "banking": [
                        ],
                        "history": [
                            f"{folder_name2}/vendor/datatables/css/jquery.dataTables.min.css",
                        ],
                        "orders": [
                        ],
                        "reports": [
                        ],
                        "user": [
                        ],
                        "content": [
                            f"{folder_name2}/vendor/bootstrap-datepicker-master/css/bootstrap-datepicker.min.css",
                        ],
                        "add_content": [
                            f"{folder_name2}/vendor/select2/css/select2.min.css",
                        ],
                        "menu": [
                            f"{folder_name2}/vendor/jqvmap/css/jqvmap.min.css",
                            f"{folder_name2}/vendor/chartist/css/chartist.min.css",
                            f"{folder_name2}/vendor/nestable2/css/jquery.nestable.min.css",
                        ],
                        "perfil_template": [
                            f"{folder_name2}/vendor/bootstrap-datepicker-master/css/bootstrap-datepicker.min.css",
                        ],
                        "add_perfil": [
                            f"{folder_name2}/vendor/select2/css/select2.min.css",
                        ],
                        "blog": [
                            f"{folder_name2}/vendor/bootstrap-datepicker-master/css/bootstrap-datepicker.min.css",
                        ],
                        "add_blog": [
                            f"{folder_name2}/vendor/select2/css/select2.min.css",
                        ],
                        "blog_category": [
                            f"{folder_name2}/vendor/bootstrap-datepicker-master/css/bootstrap-datepicker.min.css",
                        ],
                        "app_profile": [
                            f"{folder_name2}/vendor/sweetalert2/dist/sweetalert2.min.css",
                            f"{folder_name2}/vendor/lightgallery/dist/css/lightgallery.css",
                            f"{folder_name2}/vendor/lightgallery/dist/css/lg-thumbnail.css",
                            f"{folder_name2}/vendor/lightgallery/dist/css/lg-zoom.css",
                        ],
                        "edit_profile": [
                            f"{folder_name2}/vendor/bootstrap-datetimepicker/css/bootstrap-datetimepicker.min.css",
                        ],
                        "post_details": [
                            f"{folder_name2}/vendor/sweetalert2/dist/sweetalert2.min.css",
                            f"{folder_name2}/vendor/lightgallery/dist/css/lightgallery.css",
                            f"{folder_name2}/vendor/lightgallery/dist/css/lg-thumbnail.css",
                            f"{folder_name2}/vendor/lightgallery/dist/css/lg-zoom.css",
                        ],
                        "app_calender": [
                            f"{folder_name2}/vendor/fullcalendar/css/main.min.css",
                        ],
                        "chart_chartist": [
                            f"{folder_name2}/vendor/chartist/css/chartist.min.css",
                        ],
                        "chart_chartjs": [
                        ],
                        "chart_flot": [
                        ],
                        "chart_morris": [
                        ],
                        "chart_peity": [
                        ],
                        "chart_sparkline": [
                        ],
                        "ecom_checkout": [
                        ],
                        "ecom_customers": [
                        ],
                        "ecom_invoice": [
                        ],
                        "ecom_product_detail": [
                            f"{folder_name2}/vendor/star-rating/star-rating-svg.css",
                            f"{folder_name2}/vendor/owl-carousel/owl.carousel.css",
                        ],
                        "ecom_product_grid": [
                        ],
                        "ecom_product_list": [
                            f"{folder_name2}/vendor/star-rating/star-rating-svg.css",
                        ],
                        "ecom_product_order": [
                        ],
                        "perfil_compose": [
                            f"{folder_name2}/vendor/dropzone/dist/dropzone.css",
                        ],
                        "perfil_inbox": [
                        ],
                        "perfil_read": [
                        ],
                        "form_editor": [
                        ],
                        "form_element": [
                        ],
                        "form_pickers": [
                            f"{folder_name2}/vendor/bootstrap-daterangepicker/daterangepicker.css",
                            f"{folder_name2}/vendor/clockpicker/css/bootstrap-clockpicker.min.css",
                            f"{folder_name2}/vendor/jquery-asColorPicker/css/asColorPicker.min.css",
                            f"{folder_name2}/vendor/bootstrap-material-datetimepicker/css/bootstrap-material-datetimepicker.css",
                            f"{folder_name2}/vendor/pickadate/themes/default.css",
                            f"{folder_name2}/vendor/pickadate/themes/default.date.css",
                        ],
                        "form_validation": [
                        ],
                        "form_wizard": [
                            f"{folder_name2}/vendor/jquery-smartwizard/dist/css/smart_wizard.min.css",
                            f"{folder_name2}/vendor/dropzone/dist/dropzone.css",
                        ],
                        "map_jqvmap": [
                            f"{folder_name2}/vendor/jqvmap/css/jqvmap.min.css",
                        ],
                        "table_bootstrap_basic": [
                        ],
                        "table_datatable_basic": [
                            f"{folder_name2}/vendor/datatables/css/jquery.dataTables.min.css",
                            f"{folder_name2}/vendor/datatables/responsive/responsive.css",
                        ],
                        "uc_lightgallery": [
                            f"{folder_name2}/vendor/lightgallery/dist/css/lightgallery.css",
                            f"{folder_name2}/vendor/lightgallery/dist/css/lg-thumbnail.css",
                            f"{folder_name2}/vendor/lightgallery/dist/css/lg-zoom.css",
                        ],
                        "uc_nestable": [
                            f"{folder_name2}/vendor/nestable2/css/jquery.nestable.min.css",
                        ],
                        "uc_noui_slider": [
                            f"{folder_name2}/vendor/nouislider/nouislider.min.css",
                        ],
                        "uc_select2": [
                            f"{folder_name2}/vendor/select2/css/select2.min.css",
                        ],
                        "uc_sweetalert": [
                            f"{folder_name2}/vendor/sweetalert2/dist/sweetalert2.min.css",
                        ],
                        "uc_toastr": [
                            f"{folder_name2}/vendor/toastr/css/toastr.min.css",
                        ],
                        "ui_accordion": [
                        ],
                        "ui_alert": [
                        ],
                        "ui_badge": [
                        ],
                        "ui_button": [
                        ],
                        "ui_button_group": [
                        ],
                        "ui_card": [
                        ],
                        "ui_carousel": [
                        ],
                        "ui_dropdown": [
                        ],
                        "ui_grid": [
                        ],
                        "ui_list_group": [
                        ],
                        "ui_modal": [
                        ],
                        "ui_pagination": [
                        ],
                        "ui_popover": [
                        ],
                        "ui_progressbar": [
                        ],
                        "ui_tab": [
                        ],
                        "ui_typography": [
                        ],
                        "widget_basic": [
                            f"{folder_name2}/vendor/chartist/css/chartist.min.css",
                        ],
                        "page_empty": [
                        ],
                    },
                    "js":{
                        "index": [
                            f"{folder_name2}/vendor/apexchart/apexchart.js",
                            f"{folder_name2}/vendor/chart-js/chart.bundle.min.js",
                            f"{folder_name2}/vendor/counter/counter.min.js",
                            f"{folder_name2}/vendor/counter/waypoint.min.js",
                            f"{folder_name2}/vendor/peity/jquery.peity.min.js",
                            f"{folder_name2}/vendor/swiper/js/swiper-bundle.min.js",
                            f"{folder_name2}/js/dashboard/dashboard-1.js",
                        ],
                        "index_2": [
                            f"{folder_name2}/vendor/apexchart/apexchart.js",
                            f"{folder_name2}/vendor/chart-js/chart.bundle.min.js",
                            f"{folder_name2}/vendor/counter/counter.min.js",
                            f"{folder_name2}/vendor/counter/waypoint.min.js",
                            f"{folder_name2}/vendor/peity/jquery.peity.min.js",
                            f"{folder_name2}/vendor/swiper/js/swiper-bundle.min.js",
                            f"{folder_name2}/js/dashboard/dashboard-1.js",

                        ],
                        "market": [
                            f"{folder_name2}/vendor/apexchart/apexchart.js",
                            f"{folder_name2}/vendor/peity/jquery.peity.min.js",
                            f"{folder_name2}/js/dashboard/market.js",
                        ],
                        "coin_details": [
                            f"{folder_name2}/vendor/chart-js/chart.bundle.min.js",
                            f"{folder_name2}/vendor/apexchart/apexchart.js",
                            f"{folder_name2}/vendor/peity/jquery.peity.min.js",
                            f"{folder_name2}/js/dashboard/coin.js",
                            f"{folder_name2}/vendor/bootstrap-datetimepicker/js/moment.js",
                            f"{folder_name2}/vendor/bootstrap-daterangepicker/daterangepicker.js",
                        ],
                        "portfolio": [
                            f"{folder_name2}/vendor/bootstrap-datepicker-master/js/bootstrap-datepicker.min.js",
                            f"{folder_name2}/vendor/peity/jquery.peity.min.js",
                            f"{folder_name2}/vendor/apexchart/apexchart.js",
                            f"{folder_name2}/js/dashboard/portfolio.js",
                        ],
                        "ico_listing": [
                        ],
                        "p2p": [
                            f"{folder_name2}/vendor/datatables/js/jquery.dataTables.min.js",
                            f"{folder_name2}/js/plugins-init/datatables.init.js",
                        ],
                        "future": [
                            f"{folder_name2}/js/dashboard/future.js",
                            f"{folder_name2}/vendor/datatables/js/jquery.dataTables.min.js",
                            f"{folder_name2}/js/plugins-init/datatables.init.js",
                        ],
                        "trading_market": [
                            f"{folder_name2}/vendor/datatables/js/jquery.dataTables.min.js",
                            f"{folder_name2}/js/plugins-init/datatables.init.js",
                            f"{folder_name2}/vendor/chart-js/chart.bundle.min.js",
                            f"{folder_name2}/vendor/peity/jquery.peity.min.js",
                            f"{folder_name2}/js/dashboard/trading-market.js",
                        ],
                        "market_watch": [
                            f"{folder_name2}/vendor/apexchart/apexchart.js",
                            f"{folder_name2}/js/dashboard/crypto-watch.js",
                            f"{folder_name2}/vendor/swiper/js/swiper-bundle.min.js",
                        ],
                        "exchange": [	
                            f"{folder_name2}/vendor/chart-js/chart.bundle.min.js",
                            f"{folder_name2}/vendor/apexchart/apexchart.js",
                            f"{folder_name2}/js/dashboard/ticketing.js",
                        ],
                        "banking": [
                            f"{folder_name2}/vendor/chart-js/chart.bundle.min.js",
                            f"{folder_name2}/vendor/apexchart/apexchart.js",
                            f"{folder_name2}/vendor/peity/jquery.peity.min.js",
                            f"{folder_name2}/js/user.js",
                        ],
                        "history": [
                            f"{folder_name2}/vendor/datatables/js/jquery.dataTables.min.js",
                            f"{folder_name2}/js/plugins-init/datatables.init.js",
                        ],
                        "orders": [
                        ],
                        "reports": [
                        ],
                        "user": [
                        ],
                        "content": [
                            f"{folder_name2}/vendor/bootstrap-datepicker-master/js/bootstrap-datepicker.min.js",
                            f"{folder_name2}/js/dashboard/cms.js",
                        ],
                        "add_content": [
                            f"{folder_name2}/vendor/bootstrap-datepicker-master/js/bootstrap-datepicker.min.js",
                            f"{folder_name2}/vendor/ckeditor/ckeditor.js",
                            f"{folder_name2}/vendor/select2/js/select2.full.min.js",
                            f"{folder_name2}/js/plugins-init/select2-init.js",
                            f"{folder_name2}/js/dashboard/cms.js",
                        ],
                        "menu": [
                            f"{folder_name2}/js/dashboard/cms.js",
                            f"{folder_name2}/vendor/nestable2/js/jquery.nestable.min.js",
                            f"{folder_name2}/js/plugins-init/nestable-init.js",
                            f"{folder_name2}/vendor/ckeditor/ckeditor.js",
                            f"{folder_name2}/vendor/datatables/js/jquery.dataTables.min.js",
                        ],
                        "perfil_template": [
                            f"{folder_name2}/vendor/bootstrap-datepicker-master/js/bootstrap-datepicker.min.js",
                            f"{folder_name2}/js/dashboard/cms.js",
                        ],
                        "add_perfil": [
                            f"{folder_name2}/vendor/bootstrap-datepicker-master/js/bootstrap-datepicker.min.js",
                            f"{folder_name2}/vendor/ckeditor/ckeditor.js",
                            f"{folder_name2}/vendor/select2/js/select2.full.min.js",
                            f"{folder_name2}/js/plugins-init/select2-init.js",
                            f"{folder_name2}/js/dashboard/cms.js",
                        ],
                        "blog": [
                            f"{folder_name2}/vendor/bootstrap-datepicker-master/js/bootstrap-datepicker.min.js",
                            f"{folder_name2}/js/dashboard/cms.js",
                        ],
                        "add_blog": [
                            f"{folder_name2}/vendor/bootstrap-datepicker-master/js/bootstrap-datepicker.min.js",
                            f"{folder_name2}/vendor/ckeditor/ckeditor.js",
                            f"{folder_name2}/vendor/select2/js/select2.full.min.js",
                            f"{folder_name2}/js/plugins-init/select2-init.js",
                            f"{folder_name2}/js/dashboard/cms.js",
                        ],
                        "blog_category": [
                            f"{folder_name2}/vendor/bootstrap-datepicker-master/js/bootstrap-datepicker.min.js",
                            f"{folder_name2}/js/dashboard/cms.js",
                        ],
                        "app_calender": [
                            f"{folder_name2}/vendor/moment/moment.min.js",
                            f"{folder_name2}/vendor/fullcalendar/js/main.min.js",
                            f"{folder_name2}/js/plugins-init/fullcalendar-init.js",
                        ],
                        "app_profile": [
                            f"{folder_name2}/vendor/sweetalert2/dist/sweetalert2.min.js",
                            f"{folder_name2}/vendor/lightgallery/dist/lightgallery.min.js",
                            f"{folder_name2}/vendor/lightgallery/dist/plugins/thumbnail/lg-thumbnail.min.js",
                            f"{folder_name2}/vendor/lightgallery/dist/plugins/zoom/lg-zoom.min.js",
                        ],
                        "edit_profile": [
                            f"{folder_name2}/vendor/bootstrap-datepicker-master/js/bootstrap-datepicker.min.js",	
                        ],
                        "post_details": [
                            f"{folder_name2}/vendor/sweetalert2/dist/sweetalert2.min.js",	
                            f"{folder_name2}/vendor/lightgallery/dist/lightgallery.min.js",	
                            f"{folder_name2}/vendor/lightgallery/dist/plugins/thumbnail/lg-thumbnail.min.js",	
                            f"{folder_name2}/vendor/lightgallery/dist/plugins/zoom/lg-zoom.min.js",	
                        ],
                        "chart_chartist": [
                            f"{folder_name2}/vendor/chart-js/chart.bundle.min.js",
                            f"{folder_name2}/vendor/chartist/js/chartist.min.js",
                            f"{folder_name2}/vendor/chartist-plugin-tooltips/js/chartist-plugin-tooltip.min.js",
                            f"{folder_name2}/js/plugins-init/chartist-init.js",
                        ],
                        "chart_chartjs": [
                            f"{folder_name2}/vendor/chart-js/chart.bundle.min.js",
                            f"{folder_name2}/vendor/apexchart/apexchart.js",
                            f"{folder_name2}/js/plugins-init/chartjs-init.js",
                        ],
                        "chart_flot": [
                            f"{folder_name2}/vendor/flot/jquery.flot.js",
                            f"{folder_name2}/vendor/flot/jquery.flot.pie.js",
                            f"{folder_name2}/vendor/flot/jquery.flot.resize.js",
                            f"{folder_name2}/vendor/flot-spline/jquery.flot.spline.min.js",
                            f"{folder_name2}/js/plugins-init/flot-init.js",
                        ],
                        "chart_morris": [
                            f"{folder_name2}/vendor/chart-js/chart.bundle.min.js",
                            f"{folder_name2}/vendor/apexchart/apexchart.js",
                            f"{folder_name2}/vendor/morris/morris.min.js",
                            f"{folder_name2}/vendor/raphael/raphael.min.js",
                            f"{folder_name2}/js/plugins-init/morris-init.js",
                        ],
                        "chart_peity": [
                            f"{folder_name2}/vendor/peity/jquery.peity.min.js",
                            f"{folder_name2}/js/plugins-init/piety-init.js",
                        ],
                        "chart_sparkline": [
                            f"{folder_name2}/vendor/chart-js/chart.bundle.min.js",
                            f"{folder_name2}/vendor/apexchart/apexchart.js",
                            f"{folder_name2}/vendor/jquery-sparkline/jquery.sparkline.min.js",
                            f"{folder_name2}/js/plugins-init/sparkline-init.js",
                        ],
                        "ecom_checkout": [
                        ],
                        "ecom_customers": [
                            f"{folder_name2}/vendor/highlightjs/highlight.pack.min.js",
                        ],
                        "ecom_invoice": [
                        ],
                        "ecom_product_detail": [
                            f"{folder_name2}/vendor/star-rating/jquery.star-rating-svg.js",
                            f"{folder_name2}/vendor/owl-carousel/owl.carousel.js",
                        ],
                        "ecom_product_grid": [
                        ],
                        "ecom_product_list": [
                            f"{folder_name2}/vendor/star-rating/jquery.star-rating-svg.js",
                        ],
                        "ecom_product_order": [
                        ],
                        "perfil_compose": [
                            f"{folder_name2}/vendor/dropzone/dist/dropzone.js",
                        ],
                        "perfil_inbox": [
                        ],
                        "perfil_read": [
                        ],
                        "form_editor": [
                            f"{folder_name2}/vendor/ckeditor/ckeditor.js",
                        ],
                        "form_element": [
                        ],
                        "form_pickers": [
                            f"{folder_name2}/vendor/chart-js/chart.bundle.min.js",
                            f"{folder_name2}/vendor/apexchart/apexchart.js",
                            f"{folder_name2}/vendor/moment/moment.min.js",
                            f"{folder_name2}/vendor/bootstrap-daterangepicker/daterangepicker.js",
                            f"{folder_name2}/vendor/clockpicker/js/bootstrap-clockpicker.min.js",
                            f"{folder_name2}/vendor/jquery-asColor/jquery-asColor.min.js",
                            f"{folder_name2}/vendor/jquery-asGradient/jquery-asGradient.min.js",
                            f"{folder_name2}/vendor/jquery-asColorPicker/js/jquery-asColorPicker.min.js",
                            f"{folder_name2}/vendor/bootstrap-material-datetimepicker/js/bootstrap-material-datetimepicker.js",
                            f"{folder_name2}/vendor/pickadate/picker.js",
                            f"{folder_name2}/vendor/pickadate/picker.time.js",
                            f"{folder_name2}/vendor/pickadate/picker.date.js",
                            f"{folder_name2}/js/plugins-init/bs-daterange-picker-init.js",
                            f"{folder_name2}/js/plugins-init/clock-picker-init.js",
                            f"{folder_name2}/js/plugins-init/jquery-asColorPicker.init.js",
                            f"{folder_name2}/js/plugins-init/material-date-picker-init.js",
                            f"{folder_name2}/js/plugins-init/pickadate-init.js",
                        ],
                        "form_validation": [
                        ],
                        "form_wizard": [
                            f"{folder_name2}/vendor/jquery-steps/build/jquery.steps.min.js",
                            f"{folder_name2}/vendor/jquery-validation/jquery.validate.min.js",
                            f"{folder_name2}/js/plugins-init/jquery.validate-init.js",
                            f"{folder_name2}/vendor/dropzone/dist/dropzone.js",
                            f"{folder_name2}/vendor/jquery-smartwizard/dist/js/jquery.smartWizard.js",
                        ],
                        "map_jqvmap": [
                            f"{folder_name2}/vendor/jqvmap/js/jquery.vmap.min.js",
                            f"{folder_name2}/vendor/jqvmap/js/jquery.vmap.world.js",
                            f"{folder_name2}/vendor/jqvmap/js/jquery.vmap.usa.js",
                            f"{folder_name2}/js/plugins-init/jqvmap-init.js",
                        ],
                        "table_bootstrap_basic": [
                        ],
                        "table_datatable_basic": [
                            f"{folder_name2}/vendor/datatables/js/jquery.dataTables.min.js",
                            f"{folder_name2}/vendor/datatables/responsive/responsive.js",
                            f"{folder_name2}/js/plugins-init/datatables.init.js",
                        ],
                        "uc_lightgallery": [
                            f"{folder_name2}/vendor/lightgallery/dist/lightgallery.min.js",	
                            f"{folder_name2}/vendor/lightgallery/dist/plugins/thumbnail/lg-thumbnail.min.js",	
                            f"{folder_name2}/vendor/lightgallery/dist/plugins/zoom/lg-zoom.min.js",	
                        ],
                        "uc_nestable": [
                            f"{folder_name2}/vendor/nestable2/js/jquery.nestable.min.js",
                            f"{folder_name2}/js/plugins-init/nestable-init.js",
                        ],
                        "uc_noui_slider": [
                            f"{folder_name2}/vendor/nouislider/nouislider.min.js",
                            f"{folder_name2}/vendor/wnumb/wNumb.js",
                            f"{folder_name2}/js/plugins-init/nouislider-init.js",
                        ],
                        "uc_select2": [
                            f"{folder_name2}/vendor/select2/js/select2.full.min.js",
                            f"{folder_name2}/js/plugins-init/select2-init.js",
                        ],
                        "uc_sweetalert": [
                            f"{folder_name2}/vendor/sweetalert2/dist/sweetalert2.min.js",
                            f"{folder_name2}/js/plugins-init/sweetalert.init.js",
                        ],
                        "uc_toastr": [
                            f"{folder_name2}/vendor/toastr/js/toastr.min.js",
                            f"{folder_name2}/js/plugins-init/toastr-init.js",
                        ],
                        "ui_accordion": [
                            f"{folder_name2}/js/highlight.min.js",
                        ],
                        "ui_alert": [
                            f"{folder_name2}/js/highlight.min.js",
                        ],
                        "ui_badge": [
                            f"{folder_name2}/js/highlight.min.js",
                        ],
                        "ui_button": [
                            f"{folder_name2}/js/highlight.min.js",
                        ],
                        "ui_button_group": [
                            f"{folder_name2}/js/highlight.min.js",
                        ],
                        "ui_card": [
                            f"{folder_name2}/js/highlight.min.js",
                        ],
                        "ui_carousel": [
                            f"{folder_name2}/js/highlight.min.js",
                        ],
                        "ui_dropdown": [
                            f"{folder_name2}/js/highlight.min.js",
                        ],
                        "ui_grid": [
                        ],
                        "ui_list_group": [
                            f"{folder_name2}/js/highlight.min.js",
                        ],
                        "ui_modal": [
                        ],
                        "ui_pagination": [
                            f"{folder_name2}/js/highlight.min.js",
                        ],
                        "ui_popover": [
                        ],
                        "ui_progressbar": [
                            f"{folder_name2}/js/highlight.min.js",
                        ],
                        "ui_tab": [
                            f"{folder_name2}/js/highlight.min.js",
                        ],
                        "ui_typography": [
                        ],
                        "widget_basic": [
                            f"{folder_name2}/vendor/chart-js/chart.bundle.min.js",
                            f"{folder_name2}/vendor/apexchart/apexchart.js",
                            f"{folder_name2}/vendor/chartist/js/chartist.min.js",
                            f"{folder_name2}/vendor/chartist-plugin-tooltips/js/chartist-plugin-tooltip.min.js",
                            f"{folder_name2}/vendor/flot/jquery.flot.js",
                            f"{folder_name2}/vendor/flot/jquery.flot.pie.js",
                            f"{folder_name2}/vendor/flot/jquery.flot.resize.js",
                            f"{folder_name2}/vendor/flot-spline/jquery.flot.spline.min.js",
                            f"{folder_name2}/vendor/jquery-sparkline/jquery.sparkline.min.js",
                            f"{folder_name2}/js/plugins-init/sparkline-init.js",
                            f"{folder_name2}/vendor/peity/jquery.peity.min.js",
                            f"{folder_name2}/js/plugins-init/piety-init.js",
                            f"{folder_name2}/vendor/counter/counter.min.js",
                            f"{folder_name2}/vendor/counter/waypoint.min.js",
                            f"{folder_name2}/js/dashboard/dashboard-1.js",
                            f"{folder_name2}/js/plugins-init/widgets-script-init.js",
                        ],
                        "page_empty": [
                        ],
                    },
                }
            }
        }


}