import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { PacienteInComponent } from './paciente-in/paciente-in.component';
import { DocINComponent } from './doc-in/doc-in.component';
import { HomeComponent } from './home/home.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';

const routes: Routes = [
  { path: '', component: HomeComponent},
  { path: 'pacinetein', component: PacienteInComponent},
  { path: 'docin', component: DocINComponent},
  { path: '**', component: PageNotFoundComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
