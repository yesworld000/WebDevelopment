
import { Category } from './../Category';
import { categories } from './products';
import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CategoryService {

  getCategories():Observable<Category[]>
  {
    return of(categories);
  }

  getCategory(id:number): Observable<Category>
  {
      return of(categories.find(category => category.id === id));
  }

  constructor() { }
}