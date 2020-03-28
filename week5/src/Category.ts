
export interface Category
{
  name: string;
  id: number;
  products: Array<Product>;
}


export interface Product
{
  name: string;
  rating: number;
  description: string;
  image: string;
  link: string;
}