import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import {MapComponent} from '../map/index';

const routes: Routes = [
  { path: '', component: MapComponent },
  { path: 'maps', component: MapComponent },
  { path: 'dashboard', component: MapComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
