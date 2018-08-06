<template>
	<div class="home">
		<el-row>
			<el-table : data='book_list' style="width:100%" border>
				<el-table-column prop="book_name" label="shuming" min-width="100">
					<template scope="scope">{{scope.row.fields.book_name}}</template>
				</el-table-column>
			</el-table>
		</el-row>
	</div>
</template>