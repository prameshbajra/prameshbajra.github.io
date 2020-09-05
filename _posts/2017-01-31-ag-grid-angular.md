---
layout: post
title:  "Ag-Grid Angular 2+ - Create Extra Ordinary Tables/Grids"
date:   2020-09-05
desc: "Use AG-Grid for awesome tables."
keywords: "code, angular, node, web, internet, ag-grid, programming"
categories: [code, angular, node, web, internet, ag-grid, programming]
tags: [code, angular, node, web, internet, ag-grid, programming]
icon: icon-maven
---

## To start ...
<br>

with any Angular related work you will need to have Node and the Angular CLI in place. If you do not then head over to the below links to install them. 

1. [Node](https://nodejs.org/en/) (will come with npm - node package manager)
   
2. [Angular CLI](https://cli.angular.io/) 

<br>
I'm guessing that you already have an Angular project in place. This method should work with all versions of Angular that came after 2.

<br>
In case if you do not have an Angular project, then you can create it using:

```bash
ng new <project_name>
```

<br>
You will be prompted with a bunch of necessary questions where you can select necessary configuration for the project to be created.

<br>
For the demo purpose, I created a new Angular project named: ***aggrid-angular*** 
You can find the code at my github: 

<br>
[prameshbajra/aggrid-angular](https://github.com/prameshbajra/aggrid-angular)

<br>
## Starting with ag-grid
<br>
Before diving into the code, I would like to give a brief introduction on ag-grid and why I like it so much. 

The "ag" part of ag-Grid stands for "agnostic". People claim that this package is the best JavaScript Grid in the world. It is packed with lots of features and is a child's play to use, that too without any compromise in the performace. They provide highly performant, scalable tables with almost unlimited features. And guess what? .... It is totally FREE !!!

<br>
## On to the code

<br>
Start by installing the library itself.

```bash
npm install --save ag-grid-community ag-grid-angular
npm install 
```

<br>
Let's get to the actual coding! As a first step, let's add the ag-Grid Angular module to our app module (*src/app/app.module.ts*):

```tsx
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { AgGridModule } from 'ag-grid-angular';

@NgModule({
  declarations: [AppComponent],
  imports: [
    BrowserModule,
    AgGridModule.withComponents([])
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
```

<br>
The next step is to add the ag-Grid styles - replace the content of *styles.scss* with the following code:

Note: If you are under an existing Angular project then consider adding these.

```scss
@import "../node_modules/ag-grid-community/src/styles/ag-grid.scss";
@import "../node_modules/ag-grid-community/src/styles/ag-theme-alpine/sass/ag-theme-alpine-mixin.scss";

.ag-theme-alpine {
    @include ag-theme-alpine();
}
```

The code above imports the grid "structure" stylesheet (*ag-grid.css*), and one of the available grid themes: (*ag-theme-alpine.css*). The grid ships several different themes; pick one that matches your project design. You can customise it further with Sass variables too.

<br>
Next, let's declare the basic grid configuration. Edit *src/app.component.ts:*

```tsx
import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
    title = 'app';

    columnDefs = [
        {headerName: 'Make', field: 'make', sortable: true, filter: true},
        {headerName: 'Model', field: 'model', sortable: true, filter: true},
        {headerName: 'Price', field: 'price', sortable: true, filter: true}
    ];

    rowData: any;

    constructor(private http: HttpClient) {

    }

    ngOnInit() {
        this.rowData = this.http.get('https://raw.githubusercontent.com/ag-grid/ag-grid/master/grid-packages/ag-grid-docs/src/sample-data/smallRowData.json');
    }
}
```

<br>
The above code turns the rowData from a hard-coded array to an Observable. For the grid to work with it, we need to add an async pipe to the property:

```html
<ag-grid-angular
    style="width: 500px; height: 500px;"
		class="ag-theme-alpine"
		[rowData]="rowData | async"
		[columnDefs]="columnDefs">
</ag-grid-angular>
```

Just with these simple steps you can now see the table rendered in the UI. Try dragging the columns around. Nice, right? These are all the features that ag-grid provide out of the box.

<br>
## Why stop here? Let's keep adding some more stuffs

<br>
**Enable Sorting And Filtering**

Well, enabling sorting in ag-Grid is actually quite simple - all you need to do is set the sortable property to each column you want to be able to sort by. Easy isn't it? 

Click on the column heads to sort accordingly.

```tsx
columnDefs = [
    {headerName: 'Make', field: 'make', sortable: true},
    {headerName: 'Model', field: 'model', sortable: true},
    {headerName: 'Price', field: 'price', sortable: true}
];
```

<br>
As with sorting, enabling filtering is as easy as setting the filter property:

```tsx
columnDefs = [
    {headerName: 'Make', field: 'make', sortable: true, filter: true},
    {headerName: 'Model', field: 'model', sortable: true, filter: true},
    {headerName: 'Price', field: 'price', sortable: true, filter: true}
];
```