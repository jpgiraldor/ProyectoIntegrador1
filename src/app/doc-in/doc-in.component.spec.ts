import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DocINComponent } from './doc-in.component';

describe('DocINComponent', () => {
  let component: DocINComponent;
  let fixture: ComponentFixture<DocINComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DocINComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DocINComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
