
import { CategoryService } from './../category.service';
import { Category } from '../../Category';
import { categories } from './../products';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-categories',
  templateUrl: './categories.component.html',
  styleUrls: ['./categories.component.css']
})
export class CategoriesComponent implements OnInit {

  constructor(private categoryService: CategoryService) { }

  categories: Category[];
  selectedCategory: Category;

  getCategories(): void
  {
    this.categoryService.getCategories().subscribe(categories => this.categories = categories);
  }

  onSelect(category: Category): void
  {
    this.selectedCategory = category;
  }

  ngOnInit(): void {
    this.getCategories();
  }

}