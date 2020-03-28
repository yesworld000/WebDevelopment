
import { categories } from './../products';
import { CategoryService } from './../category.service';
import { Category } from './../../Category';
import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  categories: Category[] = [];

  constructor(private categoryService: CategoryService)  { }
  selectedCategory: Category;

  ngOnInit(): void {
    this.getCategories();
  }

  onSelect(category: Category): void
  {
    this.selectedCategory = category;
  }

  getCategories(): void
  {
    this.categoryService.getCategories().subscribe(categories => this.categories = categories.slice(0,5));
  }

}