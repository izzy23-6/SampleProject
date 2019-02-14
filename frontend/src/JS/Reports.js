import jsPDF from "jspdf"
import 'jspdf-autotable'
import instance from "@/api/Api"
import parse from 'date-fns/parse'
import subMinutes from 'date-fns/sub_minutes'

export default {
    name: 'Reports',
    data() {
        return {
            doc: new jsPDF('p', 'pt'),
            search: '',
            headers: [
                {
                    header: 'Date',
                    dataKey: 'trans',
                    width: 40
                },
                {
                    header: 'Item',
                    dataKey: 'productid',
                    width: 40
                },
                {
                    header: 'Description',
                    dataKey: 'Description',
                    width: 40
                },
                {
                    header: 'Unit Price',
                    dataKey: 'unitprice',
                    width: 40
                },
                {
                    header: 'Quantity',
                    dataKey: 'quantity',
                    width: 40
                },
                {
                    header: 'Total Price',
                    dataKey: 'p',
                    width: 40
                },
            ],
            patients: [],
            reportData: [],
            reportsDataTotal: null,
            selectedPatient: null,
            lastSelectedPatient: null,
            isLoadingPatients: false,
            filterDate1: null,
            filterMenu1: false,
            modal1: false,
            filterDate2: new Date().toISOString().substr(0, 10),
            filterMenu2: false,
            modal2: false,
            date: new Date().toISOString().substr(0, 10),
            time: subMinutes(parse(new Date()), 1).toLocaleTimeString(),
        }
    },
    computed: {
        apiEndPoint() {
            return this.$store.state.ReportBillingSummary.endpoints.obtainReports
        },
        reports() {
            return this.$store.state.ReportBillingSummary.reports

        },
        patientFilter() {
            /* Sets the editedItem property equal to a resident that is selected */
            if (this.patients.length > 0) {
                return {
                    FullName: this.patients[0].FullName,
                    PersonID: this.patients[0].PersonID
                }
            } else if (this.lastSelectedPatient) {
                return {
                    FullName: this.lastSelectedPatient.FullName,
                    PersonID: this.lastSelectedPatient.PersonID
                }
            } else {
                return {
                    FullName: '',
                    PersonID: ''
                }
            }
        },
    },
    created() {
    },
    watch: {
        filterMenu1(val, oldVal) {
            if (oldVal === true) {
                this.filteredCharges()
            }
        },
        filterMenu2(val, oldVal) {
            if (oldVal === true) {
                this.filteredCharges()
            }
        },
        search(val) {
            /* Event listner. This function watches the search property above. When the search properties value is change, this function runs */
            this.filterPatients()
            if (this.patients.length > 0)
                return
            if (this.isLoadingPatients) return
            this.isLoadingPatients = true
        },
        selectedPatient() {
            this.patientChange()
        },
        reports(val) {
            this.reportData = this.reports.results
            this.reportsDataTotal = this.reports.Total
        }
    },
    methods: {
        async reportsAPI() {
            const self = this
            try {
                let resp = await instance.get(`${self.$store.state.ReportBillingSummary.endpoints.obtainReports}`)
                let {
                    data: {
                        results = {}
                    }
                } = resp
                self.$store.commit('reportsAPI', results)
            } catch (err) {
                console.log(err);
            }
        },
        async filteredCharges() {
            const self = this
            try {
                let resp = await instance.get(`${self.apiEndPoint}?search_name=${self.lastSelectedPatient.FullName}&minDate=${self.filterDate1}&maxDate=${self.filterDate2}`)
                let {
                    loading
                } = resp
                self.$store.commit('reportsAPI', resp.data)
                self.loading = loading
            } catch (err) {
                console.log(err);
            }
        },
        testing: function () {
            console.log('pdf button clicked');

        },
        filterPatients: _.debounce(function () {
            /* Search query api call to server for residents */
            const self = this
            instance.get(`${"patientidsearch/?Search="}${self.search}`)
                .then((res) => {
                    const {
                        count,
                        results
                    } = res.data
                    self.patients = results
                    self.isLoadingPatients = res.loading
                })
                .catch(err => {})
        }, 100),
        patientChange: function () {
            if (this.selectedPatient) {
                this.lastSelectedPatient = this.selectedPatient
            }
            this.$nextTick(() => {
                this.selectedPatient = null
            })
        },
        printPDF: function () {
            const self = this
            const doc = self.doc

            let fontSizes = {
                HeadTitleFontSize: 18,
                Head2TitleFontSize: 16,
                TitleFontSize: 14,
                SubTitleFontSize: 12,
                NormalFontSize: 10,
                SmallFontSize: 8
            };

            let lineSpacing = {
                NormalSpacing: 12,
            };

            let rightStartCol1 = 400;
            let rightStartCol2 = 480;


            let InitialstartX = 40;
            let startX = 40;
            let InitialstartY = 50;
            let startY = 0;

            let lineHeights = 12;

            doc.setFontSize(fontSizes.SubTitleFontSize);
            doc.setFont('times');
            doc.setFontType('bold');

            var tempY = InitialstartY;

            doc.setFontType('normal');

            doc.setLineWidth(1);
            // doc.line(20, startY+lineSpacing.NormalSpacing, 580, startY+=lineSpacing.NormalSpacing);
            doc.line(40, startY + 80, 555, startY + 80);
            doc.line(40, startY + 86, 555, startY + 86);

            doc.setFontSize(fontSizes.Head2TitleFontSize + 12);
            doc.setFontType('bold');
            doc.text("Resident Billing Summary", startX + 260, startY += lineSpacing.NormalSpacing + 44, {
                align: "center"
            });

            doc.setFontSize(fontSizes.NormalFontSize);
            doc.setFontType('normal');
            doc.text(`${self.filterDate1} - ${self.filterDate2}`, startX, startY + lineSpacing.NormalSpacing + 10, {
                align: "left"
            });
            doc.setFontSize(fontSizes.NormalFontSize);
            doc.setFontType('normal');
            doc.text(`${this.date} ${this.time}`, rightStartCol2 - 25, startY += lineSpacing.NormalSpacing + 10, {
                align: "left"
            });

            doc.setFontSize(fontSizes.NormalFontSize);
            doc.setFontType('bold');

            //-------Customer Info Billing---------------------
            var startBilling = startY;

            doc.text("Billing Info:", startX, startY += lineSpacing.NormalSpacing + 28, {
                align: "left"
            });
            doc.setFontSize(fontSizes.NormalFontSize);
            doc.text("Resident", startX, startY += lineSpacing.NormalSpacing, {
                align: "left"
            });
            doc.setFontType('normal');
            doc.text(self.lastSelectedPatient.FullName, 80, startY, {
                align: "left"
            });

            doc.setFontType('bold');
            doc.text("Address", startX, startY += lineSpacing.NormalSpacing, {
                align: "left"
            });
            doc.setFontType('normal');
            doc.text(self.lastSelectedPatient.Address1, 80, startY, {
                align: "left"
            });
            doc.text(`${self.lastSelectedPatient.City} ${self.lastSelectedPatient.StateProv}, ${self.lastSelectedPatient.Country}`, 80, startY += lineSpacing.NormalSpacing, {
                align: "left"
            });
            doc.text(self.lastSelectedPatient.PostalCode, 80, startY += lineSpacing.NormalSpacing, {
                align: "left"
            });
            doc.setFontType('bold');
            doc.text("EMAIL", startX, startY += lineSpacing.NormalSpacing, {
                align: "left"
            });
            doc.setFontType('normal');
            doc.text(self.lastSelectedPatient.Email, 80, startY, {
                align: "left"
            });

            doc.setFontType('bold');
            doc.text("SS#", startX, startY += lineSpacing.NormalSpacing, {
                align: "left"
            });
            doc.setFontType('normal');
            doc.text(self.lastSelectedPatient.SSNumber, 80, startY, {
                align: "left"
            });



            //-------Customer Info Shipping---------------------
            var rightcol1 = 340;
            var rightcol2 = 400;

            startY = startBilling;
            doc.setFontType('bold');
            doc.text("Facility :", rightcol1, startY += lineSpacing.NormalSpacing + 28, {
                align: "left"
            });
            doc.setFontType('normal');
            doc.text(self.lastSelectedPatient.custparent.name, rightcol2, startY, {
                align: "left"
            });

            doc.setFontType('bold');
            doc.text("Address", rightcol1, startY += lineSpacing.NormalSpacing, {
                align: "left"
            });
            doc.setFontType('normal');
            doc.text(self.lastSelectedPatient.custparent.shiptoaddress, rightcol2, startY, {
                align: "left"
            });
            doc.text(`${self.lastSelectedPatient.custparent.shiptocity}, ${self.lastSelectedPatient.custparent.shiptostateprov}`, rightcol2, startY += lineSpacing.NormalSpacing, {
                align: "left"
            });
            doc.text(self.lastSelectedPatient.custparent.shiptopostalcode, rightcol2, startY += lineSpacing.NormalSpacing, {
                align: "left"
            });

            doc.setFontType('bold');
            doc.text("Floor/Hall", rightcol1, startY += lineSpacing.NormalSpacing, {
                align: "left"
            });
            // doc.setFontType('normal');
            // doc.text(customer_BillingInfoJSON.CustomerState, rightcol2, startY, {
            //     align: "left"
            // });

            doc.setFontType('bold');
            doc.text("Room", rightcol1, startY += lineSpacing.NormalSpacing, {
                align: "left"
            });
            // doc.setFontType('normal');
            // doc.text(customer_BillingInfoJSON.PIN, rightcol2, startY, {
            //     align: "left"
            // });

            doc.setFontType('bold');
            doc.text("Resident Number", rightcol1, startY += lineSpacing.NormalSpacing, {
                align: "left"
            });
            doc.setFontType('normal');
            doc.text(self.lastSelectedPatient.RelationReference, rightcol2 + 25, startY, {
                align: "left"
            });

            var header = function (data) {
                doc.setFontSize(8);
                doc.setTextColor(40);
                doc.setFontStyle('normal');
            };
            doc.setFontSize(8);
            doc.setFontStyle('normal');

            var options = {
                didDrawPage: header,
                margin: {
                    top: 50
                },
                styles: {
                    overflow: 'linebreak',
                    fontSize: 8,
                    minCellHeight: 'auto',
                    cellWidth: 'wrap'
                },
                columnStyles: {
                    1: {
                        cellWidth: 'auto'
                    },
                    2: {
                        cellWidth: 'auto'
                    },
                    3: {
                        cellWidth: 'auto'
                    },
                    4: {
                        cellWidth: 'auto'
                    },
                    5: {
                        cellWidth: 'auto'
                    },
                    6: {
                        cellWidth: 'auto'
                    },
                },
                startY: startY += 50
            };

            var columns = self.headers

            var rows = self.reportData

            doc.autoTable(columns, rows, options); //From dynamic data.
            // doc.autoTable(res.columns, res.data, options); //From htmlTable



            //-------Invoice Footer---------------------
            var rightcol1 = 340;
            var rightcol2 = 430;


            
            startY = doc.autoTable.previous.finalY + 25;

            doc.setLineWidth(2);
            doc.setDrawColor(0,0,0)
            // doc.line(20, startY+lineSpacing.NormalSpacing, 580, startY+=lineSpacing.NormalSpacing);
            doc.line(40, startY, 555, startY);

            doc.setFontSize(fontSizes.NormalFontSize + 5);

            doc.setFontType('bold');
            doc.text(`Total for ${self.lastSelectedPatient.FullName}:`, rightcol1 - 100, startY += lineSpacing.NormalSpacing + 5, {
                align: "left"
            });
            doc.text(`${self.reportsDataTotal}`, rightcol2 + 35, startY , {
                align: "left"
            });
            // doc.setFontSize(fontSizes.NormalFontSize);
            // doc.setFontType('bold');
            // doc.text("CGST Rs.", rightcol1, startY += lineSpacing.NormalSpacing, {
            //     align: "left"
            // });
            // doc.setFontType('normal');
            // // var w = doc.getStringUnitWidth('GSTIN') * NormalFontSize;
            // doc.text(invoiceJSON.TotalCGST, rightcol2, startY, {
            //     align: "left"
            // });


            // doc.setFontType('bold');
            // doc.text("SGST Rs.", rightcol1, startY += lineSpacing.NormalSpacing, {
            //     align: "left"
            // });
            // doc.setFontType('normal');
            // // var w = doc.getStringUnitWidth('GSTIN') * NormalFontSize;
            // doc.text(invoiceJSON.TotalSGST, rightcol2, startY, {
            //     align: "left"
            // });

            // doc.setFontType('bold');
            // doc.text("IGST Rs.", rightcol1, startY += lineSpacing.NormalSpacing, {
            //     align: "left"
            // });
            // doc.setFontType('normal');
            // // var w = doc.getStringUnitWidth('GSTIN') * NormalFontSize;
            // doc.text(invoiceJSON.TotalIGST, rightcol2, startY, {
            //     align: "left"
            // });


            // doc.setFontType('bold');
            // doc.text("CESS Rs.", rightcol1, startY += lineSpacing.NormalSpacing, {
            //     align: "left"
            // });
            // doc.setFontType('normal');
            // // var w = doc.getStringUnitWidth('GSTIN') * NormalFontSize;
            // doc.text(invoiceJSON.TotalCESS, rightcol2, startY, {
            //     align: "left"
            // });

            // doc.setFontType('bold');
            // doc.text("Total GST Rs.", rightcol1, startY += lineSpacing.NormalSpacing, {
            //     align: "left"
            // });
            // doc.setFontType('normal');
            // // var w = doc.getStringUnitWidth('GSTIN') * NormalFontSize;
            // doc.text(invoiceJSON.TotalGST, rightcol2, startY, {
            //     align: "left"
            // });


            // doc.setFontType('bold');
            // doc.text("Grand Total Rs.", rightcol1, startY += lineSpacing.NormalSpacing, {
            //     align: "left"
            // });
            // doc.setFontType('normal');
            // // var w = doc.getStringUnitWidth('GSTIN') * NormalFontSize;
            // doc.text(invoiceJSON.TotalAmnt, rightcol2, startY, {
            //     align: "left"
            // });
            // doc.setFontType('bold');
            // doc.text('For ' + comapnyJSON.CompanyName + ',', rightcol2, startY += lineSpacing.NormalSpacing + 50, {
            //     align: "center"
            // });
            // doc.text('Authorised Signatory', rightcol2, startY += lineSpacing.NormalSpacing + 50, {
            //     align: "center"
            // });

            window.open(doc.output('bloburl'), '_blank');
            // doc.save("invoice.pdf");
            }
    },
}