import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PacienteInComponent } from './paciente-in.component';

describe('PacienteInComponent', () => {
  let component: PacienteInComponent;
  let fixture: ComponentFixture<PacienteInComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PacienteInComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PacienteInComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
