---
layout: post
title:  "Use ChartsJS in your Angular2+ Project"
date:   2020-03-14
desc: "Display beautiful charts in your angular web application."
keywords: "chartsjs, ng2charts, angular8, angular, chart, web development, coding, charts, data, programming, developer"
categories: [chartsjs, ng2charts, angular8, angular, chart, web development, coding, charts, data, programming, developer]
tags: [chartsjs, ng2charts, angular8, angular, chart, web development, coding, charts, data, programming, developer]
icon: icon-fire-alt
---

How about displaying your data on a beautiful chart? They are very much favoured by almost all users and makes your website very appealing.
<br><br>

## Let's jump to the coding section.
We will be creating the application from scratch but, if in case, you need this in your existing application then feel free to jump ahead. I
will be listing down the steps and you should be good to go just by simple copy and paste. But, before that there are some prerequisites in order to continue.


### Prerequisites:

1. [NodeJS](https://nodejs.org/en/) installed.
   
2. [Angular CLI](https://cli.angular.io/) installed.


### Steps: 

1. Create a new angular project. I will be using angular 8 here but this should work for any angular application above verison 2. 

    ```
    ng new chartjs-demo
    ```

    If you are prompted with a configuration selection screen then you can select accordingly. However, I will be keeping everything as default.

2. Open the newly created project (**chartsjs-demo** in my case) in your favorite code editor.
   
3. For Angular2+ the equivalence library for [ChartsJS](https://www.chartjs.org/) is [Ng2Charts](https://valor-software.com/ng2-charts/) and here we will be using the same. I will also be referring the **Ng2Charts** documentation for installing and setting up the charts.
   
4. Open a terminal in your current project folder and execute the following command.

    ```
    npm install --save ng2-charts
    npm install --save chart.js
    ```

5. The above step will install ChartJS library into your angular application. We need to import it as a module now. We do what we always do to import modules in angular. Import it in `app.module.ts` file.

    ```javascript
    import { ChartsModule } from 'ng2-charts';

    // In your App's module:
    imports: [
      ChartsModule
    ]
    ```

    Just to be sure we are not bombarded with errors we can check our application in the browser by running `ng serve -o`.

5. A starter screen should automatically open and you should be able to see angular screen. 

6. Now, moving on to the charts part. I will be creating the charts right at the `App Component`. So, to do this we can remove all existing code in `app.component.html` and add this snippet for rendering charts.

    ```html
    <div>
        <div>
            <div class="chart">
            <canvas baseChart [data]="pieChartData" [labels]="pieChartLabels"
                [chartType]="pieChartType" [options]="pieChartOptions" [colors]="pieChartColors" [legend]="pieChartLegend">
            </canvas>
            </div>
        </div>
    </div>
    ```

    Similarly, in `app.component.ts` file you can replace the existing code with:

    ```typescript
    import { Component } from '@angular/core';
    import { ChartType, ChartOptions } from 'chart.js';
    import { Label } from 'ng2-charts';

    @Component({
        selector: 'app-root',
        templateUrl: './app.component.html',
        styleUrls: ['./app.component.scss']
    })
    export class AppComponent {
        title = 'chartjs';

        public pieChartOptions: ChartOptions = {
            responsive: true,
            legend: {
                position: 'top',
            },
            plugins: {
                datalabels: {
                    formatter: (value, ctx) => {
                        const label = ctx.chart.data.labels[ctx.dataIndex];
                        return label;
                    },
                },
            }
        };
        public pieChartLabels: Label[] = [['PUBG'], ['Fortnite'], ['Call of Duty']];
        public pieChartData: number[] = [300, 500, 100];
        public pieChartType: ChartType = 'pie';
        public pieChartLegend = true;
        public pieChartColors = [
            {
                backgroundColor: ['rgba(255,0,0,0.3)', 'rgba(0,255,0,0.3)', 'rgba(0,0,255,0.3)'],
            },
        ];

    }
    ```

7. Switch back to your browser and you should see something like this.

    ![Chart JS chart](https://www.freakyjolly.com/wp-content/uploads/2020/05/Pasted-into-Angular-98-Chart-Js-Tutorial-using-ng2-charts-with-Examples-4.png)

8. Congratutions, we are done. The charts are at your disposal.
<br><br>




It was easy isn't it? But it is very rare that your requirements will be this limited and abstract.
<br><br>
The chart we did here is just the tip of an iceberg. There are lots of other charts like line charts, bar charts, doughnut charts and scatter plots which you could make use of. All the available charts are present in [this documentation](https://valor-software.com/ng2-charts/#/GeneralInfo). These charts are very customizable and configurable but unfortunately not all options are available in the documentation above. For more options regarding the configurations, you might want to have a look at [CHARTJS Docs](https://www.chartjs.org/docs/latest/). Other entities might be different but the **ChartOptions** are exactly the same.
<br><br>
Hope this helps! Happy Coding!
<br><br><br>




> As always, feel free to get in touch if you need any help.